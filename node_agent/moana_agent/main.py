from argparse import ArgumentParser
import time
import json
import sys
import os
import logging

import requests

from moana_agent.agentutils import logging_setup, logf, \
    RECEIVED, COMPLETED_STATES, SUCCESS, FAILURE
from moana_agent import handlers


def get_new_nodetasks(args):
    resp = requests.get("%s/api/v1/nodes/%s/tasks" % (args.url, args.nodeid))
    if resp.status_code == 200:
        return resp.json()

    logging.error(logf("API Error", code=resp.status_code))
    sys.exit(1)


def update_nodetask_state(args, nodetask, state):
    if isinstance(state, str):
        state = (state, {})

    response = {
        "state": state[0]
    }
    if state[0] in COMPLETED_STATES:
        if state[1] != '':
            key = "data" if SUCCESS else "error"
            response["response"] = json.dumps({
                key: state[1]
            })

    resp = requests.put(
        "%s/api/v1/nodes/%s/tasks/%s" %(args.url, args.nodeid, nodetask["id"]),
        json={
            "task": response
        }
    )
    if resp.status_code != 200:
        logging.error(logf("Failed to update Received status",
                           code=resp.status_code))
        sys.exit(1)


def get_args():
    parser = ArgumentParser()
    parser.add_argument("--url", help="Moana Server URL")
    parser.add_argument("nodeid", help="Node ID")
    parser.add_argument("--interval", type=int, default=2,
                        help="Task check interval")
    parser.add_argument("--verbose", action="store_true",
                        help="Verbose log")
    args = parser.parse_args()
    if args.url is None:
        url = os.environ.get("MOANA_URL", None)
        if url is None:
            logging.error("Environment variable \"MOANA_URL\" is "
                          "not set or \"--url\" is not specified")
            sys.exit(1)
        else:
            args.url = url

    args.url = args.url.strip("/")
    return args


def handle_task(args, nodetask):
    tasktype = nodetask["task"]["type"].lower()
    func = getattr(handlers, "handle_" + tasktype, None)
    if func is not None:
        try:
            nodetask["task"]["data"] = json.loads(nodetask["task"]["data"])
            return func(args, nodetask)
        except Exception as err:
            # Any unhandled exception in handler is Task Failure
            return (FAILURE, err)

    logging.warning(logf("Not implemented", task_type=tasktype))

    # No change, return same state
    return nodetask["state"]


def listen(args):
    while True:
        # get messages
        nodetasks = get_new_nodetasks(args)
        for nodetask in nodetasks["data"]:
            if nodetask["state"] in COMPLETED_STATES:
                logging.debug(logf("Ignoring already completed task",
                                   task_id=nodetask["task"]["id"]))
                continue

            update_nodetask_state(args, nodetask, RECEIVED)
            logging.debug(logf("Doing task..", task_id=nodetask["task"]["id"]))

            response_state = handle_task(args, nodetask)
            state = response_state
            if not isinstance(response_state, str):
                state = response_state[0]

            if state != nodetask["state"]:
                logging.debug(logf("Task completed",
                                   task_id=nodetask["task"]["id"],
                                   state=response_state))
                update_nodetask_state(args, nodetask, response_state)

        time.sleep(args.interval)


def main():
    try:
        args = get_args()
        logging_setup(args)
        listen(args)

    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    main()

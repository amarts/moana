from argparse import ArgumentParser
import time
import json
import sys

import requests


def get_new_messages():
    resp = requests.get("http://localhost:4000/api/v1/nodes/%s/tasks" % sys.argv[1])
    if resp.status_code == 200:
        return resp.json()
    print(resp.status_code)
    sys.exit(1)


def update_message_state(message, state):
    resp = requests.put(
        "http://localhost:4000/api/v1/nodes/%s/tasks/%s" %(sys.argv[1], message["id"]),
        json={
            "task": {"state": state}
        }
    )
    if resp.status_code != 200:
        print("Failed to update Received status")
        sys.exit(1)


def main():
    while True:
        # get messages
        messages = get_new_messages()
        for message in messages["data"]:
            if message["state"] in ["Success", "Failed"]:
                print("Ignoring already completed task(Task ID: %s)" % message["task"]["id"])
                continue
            update_message_state(message, "Received")
            print("Doing task..(Task ID: %s)" % message["task"]["id"])
            time.sleep(1)
            print("Task completed(Task ID: %s)" % message["task"]["id"])
            print("Task: ")
            print(json.dumps(json.loads(message["task"]["data"]), indent=2))
            update_message_state(message, "Success")

        time.sleep(2)


if __name__ == "__main__":
    main()

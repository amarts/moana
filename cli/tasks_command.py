import json

import requests


def task_row(task):
    data = json.loads(task["data"])
    row = []
    for k, v in data.items():
        if isinstance(v, str):
            row.append("%s=%s" % (k, v))
    return "%-36s  %-10s  %-15s  %s" % (
        task["id"],
        task["state"],
        task["type"],
        " ".join(row)
    )


def node_task_row(nodetask):
    return "%-36s  %-10s  %-36s  %s" % (
        nodetask["id"],
        nodetask["state"],
        nodetask["node"]["id"],
        nodetask["node"]["hostname"]
    )


def display_tasks(tasks):
    print("%-36s  %-10s  %-15s  %s" % ("Task ID", "State", "Type", "Details"))
    for task in tasks:
        print(task_row(task))


def display_task(task):
    print("%-36s  %-10s  %-15s  %s" % ("Task ID", "State", "Type", "Details"))
    print(task_row(task))
    print()
    print()
    print("%-36s  %-10s  %-36s  %s" % ("Node Task ID", "State", "Node ID", "Hostname"))
    for nodetask in task["nodetasks"]:
        print(node_task_row(nodetask))


def set_args_get_tasks(parser):
    parser.add_argument("--cluster-id", required=True)
    parser.add_argument("--task-id")


def run_get_tasks(args):
    print()
    url = "%s/api/v1/clusters/%s/tasks" % (args.url, args.cluster_id)
    if args.task_id:
        url += "/" + args.task_id
    resp = requests.get(url)
    if resp.status_code == 200:
        if args.task_id:
            display_task(resp.json()["data"])
        else:
            display_tasks(resp.json()["data"])
    else:
        print(resp.status_code)

import json

import requests

from moana.cliutils import get_cluster_id, cluster_id_none_failure


def task_row(task):
    data = json.loads(task["data"])
    row = []
    for key, val in data.items():
        if isinstance(val, str):
            row.append("%s=%s" % (key, val))
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


def set_args(subparser):
    task_parser = subparser.add_parser('task')
    task_subparser = task_parser.add_subparsers(dest="subcmd")

    cmd_list = task_subparser.add_parser("list")
    cmd_list.add_argument("--cluster", "-c", help="Cluster name or ID")
    cmd_list.add_argument("--task-id", "-t", help="Task ID")


def subcmd_list(args):
    cluster_id = get_cluster_id(args.cluster, default=True)
    cluster_id_none_failure(cluster_id)
    print()
    url = "%s/api/v1/clusters/%s/tasks" % (args.url, cluster_id)
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

import requests

from moana.cliutils import get_cluster_id, failure, \
    cluster_id_none_failure, cluster_by_id


def set_args(subparser):
    volume_parser = subparser.add_parser('volume')
    volume_subparser = volume_parser.add_subparsers(dest="subcmd")

    cmd_create = volume_subparser.add_parser("create")
    cmd_create.add_argument("name", help="Volume Name")
    cmd_create.add_argument("--cluster", "-c", help="Cluster Name or ID")
    cmd_create.add_argument("bricks", nargs="+")

    cmd_list = volume_subparser.add_parser("list")
    cmd_list.add_argument("--volume", help="Volume Name or ID")
    cmd_list.add_argument("--cluster", "-c", help="Cluster Name or ID")


def prepare_bricks_list(cluster_id, data):
    cluster_info = cluster_by_id(cluster_id)
    if cluster_info is None:
        failure("Invalid Cluster ID or name")

    nodedata = {}
    for node in cluster_info["nodes"]:
        nodedata[node["hostname"]] = node["id"]

    bricks = []
    for item in data:
        node_hostname, brick_path = item.split(":")
        node_id = nodedata.get(node_hostname, None)
        if node_id is None:
            failure("Invalid node %s" % node_hostname)

        bricks.append(
            {
                "node_id": node_id,
                "path": brick_path
            }
        )
    return bricks


def subcmd_create(args):
    cluster_id = get_cluster_id(args.cluster, default=True)
    cluster_id_none_failure(cluster_id)
    url = "%s/api/v1/clusters/%s/volumes" % (args.url, cluster_id)
    resp = requests.post(
        url,
        json={
            "volume": {
                "name": args.name,
                "bricks": prepare_bricks_list(cluster_id, args.bricks)
            }
        }
    )
    if resp.status_code == 201:
        print("Volume creation request sent")
        print("Task ID: %s" % resp.json()["data"]["id"])
    else:
        print(resp.status_code)


def subcmd_list(args):
    cluster_id = get_cluster_id(args.cluster, default=True)
    cluster_id_none_failure(cluster_id)
    url = "%s/api/v1/clusters/%s/volumes" % (args.url, cluster_id)
    resp = requests.get(url)
    if resp.status_code == 200:
        print("%-36s  %-15s %-15s %s" % ("ID", "Name", "Type", "State"))
        for vol in resp.json()["data"]:
            print("%-36s  %-15s %-15s %-s" % (vol["id"], vol["name"], vol["type"], vol["state"]))
    else:
        print(resp.status_code)

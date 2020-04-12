import requests

from moana.cliutils import failure, get_cluster_id, cluster_id_none_failure


def set_args(subparser):
    node_parser = subparser.add_parser('node')
    node_subparser = node_parser.add_subparsers(dest="subcmd")

    cmd_list = node_subparser.add_parser("list")
    cmd_list.add_argument("--cluster", "-c", help="Cluster Name or ID")
    cmd_list.add_argument("--node", "-n", help="Node Name or ID")

    cmd_join = node_subparser.add_parser("join")
    cmd_join.add_argument("--cluster", "-c", help="Cluster Name or ID")
    cmd_join.add_argument("hostname", help="Hostname")

    cmd_leave = node_subparser.add_parser("leave")
    cmd_leave.add_argument("--cluster", "-c", help="Cluster Name or ID")
    cmd_leave.add_argument("node", help="Node Hostname or ID")

    cmd_update = node_subparser.add_parser("update")
    cmd_update.add_argument("hostname", help="Hostname")
    cmd_update.add_argument("--cluster", "-c", help="Cluster name or ID")
    cmd_update.add_argument("--node", required=True, help="Node Hostname or ID")


def subcmd_list(args):
    cluster_id = get_cluster_id(args.cluster, default=True)
    cluster_id_none_failure(cluster_id)
    resp = requests.get(args.url + "/api/v1/clusters/" + cluster_id + "/nodes")
    if resp.status_code == 200:
        print("%36s  %36s  %s" % ("Cluster", "Node ID", "Hostname"))
        for node in resp.json()["data"]:
            print("%36s  %36s  %s" % (cluster_id, node["id"], node["hostname"]))
    else:
        failure("API Error: %s" % resp.status_code)


def subcmd_join(args):
    cluster_id = get_cluster_id(args.cluster, default=True)
    cluster_id_none_failure(cluster_id)
    resp = requests.post(
        args.url + "/api/v1/clusters/" + cluster_id + "/nodes",
        json={
            "node": {
                "hostname": args.hostname
            }
        }
    )
    if resp.status_code == 201:
        print("Node added to Cluster successfully")
        print("Node ID: %s" % resp.json()["data"]["id"])
    else:
        print(resp.status_code)


def subcmd_leave(args):
    cluster_id = get_cluster_id(args.cluster, default=True)
    cluster_id_none_failure(cluster_id)
    resp = requests.delete(
        args.url + "/api/v1/clusters/" + cluster_id + "/nodes/" + args.node
    )
    if resp.status_code == 204:
        print("Node deleted successfully")
    else:
        print(resp.status_code)


def subcmd_update(args):
    # cluster_id = get_cluster_id(args.cluster, default=True)
    # cluster_id_none_failure(cluster_id)
    # resp = requests.put(
    #     args.url + "/api/v1/clusters/" + cluster_id + "/nodes/" + args.node_id,
    #     json={
    #         "node": {
    #             "hostname": args.hostname
    #         }
    #     }
    # )
    # if resp.status_code == 200:
    #     print("Node details updated successfully")
    # else:
    #     print(resp.status_code)
    pass

import requests

from moana.cliutils import failure, get_default_cluster_id, \
    save_local_cluster_list, get_cluster_id, set_default_cluster_id, \
    remove_default_cluster_id, sync_clusters_info


def set_args(subparser):
    cluster_parser = subparser.add_parser('cluster')
    cluster_subparser = cluster_parser.add_subparsers(dest="subcmd")

    cmd_list = cluster_subparser.add_parser("list")
    cmd_list.add_argument("--cluster", "-c", help="Cluster Name or ID")

    cmd_set_default = cluster_subparser.add_parser("set-default")
    cmd_set_default.add_argument("cluster", help="Cluster Name or ID")

    cmd_create = cluster_subparser.add_parser("create")
    cmd_create.add_argument("name")

    cmd_delete = cluster_subparser.add_parser("delete")
    cmd_delete.add_argument("cluster", help="Cluster Name or ID")

    cmd_update = cluster_subparser.add_parser("update")
    cmd_update.add_argument("--cluster", "-c", required=True, help="Cluster Name or ID")
    cmd_update.add_argument("--name", required=True, help="Cluster Name")


def subcmd_create(args):
    resp = requests.post(
        args.url + "/api/v1/clusters",
        json={
            "cluster": {
                "name": args.name
            }
        }
    )
    if resp.status_code == 201:
        sync_clusters_info(args)
        print("Cluster created successfully")
        print("Cluster ID: %s" % resp.json()["data"]["id"])
    else:
        failure("API Error: %s" % resp.status_code)


def subcmd_delete(args):
    cluster_id = get_cluster_id(args.cluster)
    if cluster_id is None:
        failure("Invalid Cluster name or ID")

    resp = requests.delete(args.url + "/api/v1/clusters/" + cluster_id)
    if resp.status_code == 204:
        if get_default_cluster_id() == cluster_id:
            remove_default_cluster_id()

        print("Cluster deleted successfully")
    else:
        failure("API Error: %s" % resp.status_code)


def subcmd_update(args):
    cluster_id = get_cluster_id(args.cluster)
    if cluster_id is None:
        failure("Invalid Cluster name or ID")

    resp = requests.put(
        args.url + "/api/v1/clusters/" + cluster_id,
        json={
            "cluster": {
                "name": args.name
            }
        }
    )
    if resp.status_code == 200:
        print("Cluster updated successfully")
    else:
        failure("API Error: %s" % resp.status_code)


def subcmd_set_default(args):
    cluster_id = get_cluster_id(args.cluster)
    set_default_cluster_id(cluster_id)
    print("Default Cluster ID set successfully")


def subcmd_list(args):
    suffix = ""
    if args.cluster:
        cluster_id = get_cluster_id(args.cluster)
        if cluster_id is None:
            failure("Invalid Cluster name or ID")

        suffix = "/" + cluster_id

    resp = requests.get(args.url + "/api/v1/clusters" + suffix)
    if resp.status_code == 200:
        print("%37s  %s" % ("ID", "Name"))
        data = resp.json()["data"]
        if isinstance(data, dict):
            print("%s  %s" % (data["id"], data["name"]))
        else:
            default_cluster_id = get_default_cluster_id()
            save_local_cluster_list(data)
            for cluster in data:
                print("%s%s  %s" % (
                    "*" if default_cluster_id == cluster["id"] else " ",
                    cluster["id"],
                    cluster["name"]
                ))
    else:
        failure("API Error: %s" % resp.status_code)

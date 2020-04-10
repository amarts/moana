import requests


def set_args(parser):
    parser.add_argument("--cluster-id", required=True, help="Cluster ID")
    parser.add_argument("--node-id", help="Node ID")


def run(args):
    suffix = "" if args.node_id is None else "/" + args.node_id
    resp = requests.get(args.url + "/api/v1/clusters/" + args.cluster_id + "/nodes" + suffix)
    if resp.status_code == 200:
        print("%36s  %s" % ("ID", "Hostname"))
        data = resp.json()["data"]
        if isinstance(data, dict):
            print("%s  %s" % (data["id"], data["hostname"]))
        else:
            for node in data:
                print("%s  %s" % (node["id"], node["hostname"]))
    else:
        print(resp.status_code)

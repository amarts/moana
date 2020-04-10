import requests


def set_args(parser):
    parser.add_argument("hostname", help="Hostname")
    parser.add_argument("--cluster-id", required=True, help="Cluster ID")
    parser.add_argument("--node-id", required=True, help="Node ID")


def run(args):
    resp = requests.put(args.url + "/api/v1/clusters/" + args.cluster_id + "/nodes/" + args.node_id,
                        json={
                            "node": {
                                "hostname": args.hostname
                            }
                        }
    )
    if resp.status_code == 200:
        print("Node details updated successfully")
    else:
        print(resp.status_code)

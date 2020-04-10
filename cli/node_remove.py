import requests


def set_args(parser):
    parser.add_argument("--cluster-id", required=True, help="Cluster ID")
    parser.add_argument("--node-id", required=True, help="Node ID")


def run(args):
    resp = requests.delete(args.url + "/api/v1/clusters/" + args.cluster_id + "/nodes/" + args.node_id)
    if resp.status_code == 204:
        print("Node deleted successfully")
    else:
        print(resp.status_code)

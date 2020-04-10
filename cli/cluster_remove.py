import requests


def set_args(parser):
    parser.add_argument("--cluster-id", required=True, help="Cluster ID")


def run(args):
    resp = requests.delete(args.url + "/api/v1/clusters/" + args.cluster_id)
    if resp.status_code == 204:
        print("Cluster deleted successfully")
    else:
        print(resp.status_code)

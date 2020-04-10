import requests


def set_args(parser):
    parser.add_argument("hostname", help="Hostname")
    parser.add_argument("--cluster-id", required=True, help="Cluster ID")


def run(args):
    resp = requests.post(args.url + "/api/v1/clusters/" + args.cluster_id + "/nodes",
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

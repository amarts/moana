import requests


def set_args(parser):
    parser.add_argument("name", help="Cluster Name")
    parser.add_argument("--cluster-id", required=True, help="Cluster ID")


def run(args):
    resp = requests.put(args.url + "/api/v1/clusters/" + args.cluster_id,
                        json={
                            "cluster": {
                                "name": args.name
                            }
                        }
    )
    if resp.status_code == 200:
        print("Cluster updated successfully")
    else:
        print(resp.status_code)

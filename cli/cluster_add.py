import requests


def set_args(parser):
    parser.add_argument("name", help="Cluster Name")


def run(args):
    resp = requests.post(args.url + "/api/v1/clusters",
                         json={
                             "cluster": {
                                 "name": args.name
                             }
                         }
    )
    if resp.status_code == 201:
        print("Cluster created successfully")
        print("Cluster ID: %s" % resp.json()["data"]["id"])
    else:
        print(resp.status_code)

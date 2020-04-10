import requests


def set_args(parser):
    parser.add_argument("--cluster-id", help="Cluster ID")


def run(args):
    suffix = "" if args.cluster_id is None else "/" + args.cluster_id
    resp = requests.get(args.url + "/api/v1/clusters" + suffix)
    if resp.status_code == 200:
        print("%36s  %s" % ("ID", "Name"))
        data = resp.json()["data"]
        if isinstance(data, dict):
            print("%s  %s" % (data["id"], data["name"]))
        else:
            for cluster in data:
                print("%s  %s" % (cluster["id"], cluster["name"]))
    else:
        print(resp.status_code)

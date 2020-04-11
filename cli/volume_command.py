import requests


def set_args_volume_create(parser):
    parser.add_argument("name", help="Volume Name")
    parser.add_argument("--cluster-id", required=True)
    parser.add_argument("bricks", nargs="+")


def prepare_bricks_list(data):
    bricks = []
    for item in data:
        node_id, brick_path = item.split(":")
        bricks.append(
            {
                "node_id": node_id,
                "path": brick_path
            }
        )
    return bricks


def run_volume_create(args):
    url = "%s/api/v1/clusters/%s/volumes" % (args.url, args.cluster_id)
    resp = requests.post(url,
                         json={
                             "volume": {
                                 "name": args.name,
                                 "bricks": prepare_bricks_list(args.bricks)
                             }
                         }
    )
    if resp.status_code == 201:
        print("Volume creation request sent")
        print("Task ID: %s" % resp.json()["data"]["id"])
    else:
        print(resp.status_code)

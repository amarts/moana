import sys
import os
import uuid
import json

import requests

CLUSTERS_FILE = os.path.join(os.environ["HOME"], ".moana/clusters.json")
DEFAULT_CLUSTER_FILE = os.path.join(os.environ["HOME"], ".moana/default_cluster")


def cluster_id_none_failure(cluster_id):
    if cluster_id is None:
        failure("Invalid Cluster name or ID")


def failure(message, ret=1):
    print(message, file=sys.stderr)
    sys.exit(ret)


def create_moana_dir():
    try:
        os.mkdir(os.path.join(os.environ["HOME"], ".moana"))
    except FileExistsError:
        pass


def get_subcmd_name(args):
    subcmd = getattr(args, "subcmd", None)
    if subcmd is None:
        return None

    return "subcmd_" + subcmd.replace("-", "_")


def is_uuid(val):
    try:
        uuid.UUID(val)
        return True
    except ValueError:
        return False


def get_local_cluster_list():
    if not os.path.exists(CLUSTERS_FILE):
        return None

    with open(CLUSTERS_FILE) as cfile:
        return json.load(cfile)

    return []


def save_local_cluster_list(data):
    with open(CLUSTERS_FILE, "w") as cfile:
        cfile.write(json.dumps(data))


def get_default_cluster_id():
    if not os.path.exists(DEFAULT_CLUSTER_FILE):
        return None

    with open(DEFAULT_CLUSTER_FILE) as cfile:
        return cfile.read().strip()

    return None


def set_default_cluster_id(cluster_id):
    with open(DEFAULT_CLUSTER_FILE, "w") as cfile:
        return cfile.write(cluster_id)


def remove_default_cluster_id():
    try:
        os.remove(DEFAULT_CLUSTER_FILE)
    except FileNotFoundError:
        pass


def cluster_by_name(name):
    clusters = get_local_cluster_list()
    for cluster in clusters:
        if cluster["name"] == name:
            return cluster

    return None


def cluster_by_id(cluster_id):
    clusters = get_local_cluster_list()
    for cluster in clusters:
        if cluster["id"] == cluster_id:
            return cluster

    return None


def get_cluster_id(val, default=False):
    if val is None:
        if default:
            return get_default_cluster_id()

        return None

    if is_uuid(val):
        return val

    cluster = cluster_by_name(val)
    if cluster is not None:
        return cluster["id"]

    return None


def sync_clusters_info(args):
    resp = requests.get(args.url + "/api/v1/clusters")
    if resp.status_code == 200:
        data = resp.json()["data"]
        save_local_cluster_list(data)
    else:
        failure("Failed to cache clusters list")

from argparse import ArgumentParser

import requests

import cluster_add
import cluster_update
import cluster_remove
import cluster_list
import node_add
import node_update
import node_remove
import node_list


def main():
    parser = ArgumentParser()
    parser.add_argument("--url", required=True, help="URL of Control Plane")
    subparsers = parser.add_subparsers(dest="mode")

    cluster_add.set_args(subparsers.add_parser('cluster-add'))
    cluster_list.set_args(subparsers.add_parser('cluster-list'))
    cluster_remove.set_args(subparsers.add_parser('cluster-remove'))
    cluster_update.set_args(subparsers.add_parser('cluster-update'))

    node_add.set_args(subparsers.add_parser('node-add'))
    node_list.set_args(subparsers.add_parser('node-list'))
    node_remove.set_args(subparsers.add_parser('node-remove'))
    node_update.set_args(subparsers.add_parser('node-update'))
    
    args = parser.parse_args()
    args.url = args.url.strip("/")
    modname = args.mode.replace("-", "_")
    module = globals().get(modname, None)
    if module is not None:
        module.run(args)
    else:
        print("Invalid command")


if __name__ == "__main__":
    main()

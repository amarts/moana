from argparse import ArgumentParser
import os

from moana import login_commands
from moana import cluster_commands
from moana import node_commands
from moana import task_commands
from moana import volume_commands
from moana.cliutils import failure, create_moana_dir, get_subcmd_name


def set_subcommands(subparsers):
    modules = [
        login_commands,
        cluster_commands,
        node_commands,
        task_commands,
        volume_commands
    ]
    for module in modules:
        module.set_args(subparsers)


def main():
    parser = ArgumentParser()
    parser.add_argument("--url", help="URL of Control Plane")
    subparsers = parser.add_subparsers(dest="mode")
    set_subcommands(subparsers)

    args = parser.parse_args()
    if args.url is None:
        args.url = os.environ.get("MOANA_URL", None)
        if args.url is None:
            failure("Environment variable \"MOANA_URL\" is "
                    "not set or \"--url\" is not specified")

    args.url = args.url.strip("/")
    modname = args.mode.replace("-", "_")
    module = globals().get(modname + "_commands", None)

    create_moana_dir()

    if module is not None:
        cmd = get_subcmd_name(args)
        if cmd is not None:
            # Second level subcommand, For example
            # moana cluster list
            func = getattr(module, cmd, None)
            if func is None:
                failure("Invalid %s command" % args.mode)

            func(args)
        else:
            # No second level subcommand, call the main
            # function itself
            func = getattr(module, "main", None)
            if func is not None:
                module.main(args)
            else:
                failure("Invalid command")
    else:
        failure("Invalid command")


if __name__ == "__main__":
    main()

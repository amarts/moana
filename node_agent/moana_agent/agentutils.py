import logging
import sys


QUEUED = "Queued"
RECEIVED = "Received"
SUCCESS = "Success"
FAILURE = "Failure"

COMPLETED_STATES = [SUCCESS, FAILURE]


def logf(msg, **kwargs):
    """Formats message for Logging"""
    msgparts = []
    for msg_key, msg_value in kwargs.items():
        msgparts.append("{%s=%s}" % (msg_key, msg_value))

    return "%s %s" % (msg, ", ".join(msgparts))


def logging_setup(args):
    """Logging Setup"""
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    if args.verbose:
        root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(logging.INFO)
    if args.verbose:
        handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s "
                                  "[%(module)s-%(lineno)s:%(funcName)s] "
                                  "- %(message)s")
    handler.setFormatter(formatter)
    root.addHandler(handler)

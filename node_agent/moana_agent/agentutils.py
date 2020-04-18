import logging
import sys


class TaskState:
    Queued = "Queued"
    Received = "Received"
    Success = "Success"
    Failure = "Failure"

    @classmethod
    def completed_states(cls):
        return [cls.Success, cls.Failure]


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

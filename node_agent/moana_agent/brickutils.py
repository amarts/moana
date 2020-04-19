import logging
import sys
import os

from .agentutils import logf

def  validate_brick_create(brick):
    ret = True
    path = brick['path']

    try:
        return os.mkdirdirs(path)
    except OSError as error:
        # Check Specific error
        print(error)
        try:
            if not os.listdir(path):
                return True
        except OSError as err:
            print(err)
    return False

import logging

from moana_agent.brickutils import validate_brick_create
from moana_agent.agentutils import SUCCESS, FAILURE, logf

def handle_volume_create(args, nodetask):
    """Handle Volume create"""
    print(args)
    print(nodetask)

    is_success = False
    node_id = nodetask['node_id']
    bricks = nodetask['task']['data']['bricks']

    for brick in bricks:
        if brick['node_id'] != node_id:
            continue

        is_success = validate_brick_create(brick)

    return is_success ? SUCCESS: FAILURE


def handle_volume_create_start(args, nodetask):
    """Alias of handle_volume_create"""
    return handle_volume_create(args, nodetask)

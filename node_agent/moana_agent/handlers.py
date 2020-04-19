import logging

from moana_agent.agentutils import SUCCESS, FAILURE, logf


def handle_volume_create(args, nodetask):
    """Handle Volume create"""
    return SUCCESS


def handle_volume_create_start(args, nodetask):
    """Alias of handle_volume_create"""
    return handle_volume_create(args, nodetask)

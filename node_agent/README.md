## Usage

```
$ sudo pip3 install requests
$ cd node_agent
$ python3 -m moana_agent.main <node-id> --verbose
```

## Implementing new functionality

In `$SRC/node_agent/moana_agent/handlers.py`, add a function with name
as `handle_<action>`. For example,

```
def handle_volume_create(args, nodetask):
    ...
```

* `args`     - arguments passed to node agent
* `nodetask` - details about the task.

Example `nodetask`:

```
{
    'id': '10c19aa0-ac89-4112-903e-a916c18734fa',
    'node_id': '624a0c71-c76d-4d71-9f40-239894a25ce3',
    'state': 'Queued',
    'task': {
        'data': {
            'bricks': [
              {'node_id': '624a0c71-c76d-4d71-9f40-239894a25ce3', 'path': '/bricks/b1'}
            ],
            'name': 'gvol7'
        },
        'id': '62173058-66ee-45ea-ba07-f8a83538d7e4',
        'state': 'Queued',
        'type': 'volume_create'
    }
}
```

Node agent will have access to full task data, but it should implement
only local changes required. For example, Create brick directory only
if brick's node ID matches with node agent's node ID(`args.nodeid`).

## Sending Response

Handler function can return two states and alternatively response
message or dict. For example,

```
def handle_volume_create(args, nodetask):
    ...
    return TaskState.Success
```

or

```
def handle_volume_create(args, nodetask):
    ...
    return (TaskState.Failure, {
        "message": "brick is already part of another volume",
        "path": "/bricks/b1"
    })
```

## Logging

Use `logf` for structured logging.

```
logging.info(logf("brick directory is created", path="/bricks/b1"))
```

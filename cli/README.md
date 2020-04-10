## Cluster Add

```
$ python3 main.py --url http://localhost:4000 \
    cluster-add mycluste
Cluster created successfully
Cluster ID: 56ccd3cb-cb2d-40a6-a622-6a94543295e5
```

## Cluster Update

```
$ python3 main.py --url http://localhost:4000 \
    cluster-update mycluster \
    --cluster-id 56ccd3cb-cb2d-40a6-a622-6a94543295e5
Cluster updated successfully
```

## Cluster List

```
$ python3 main.py --url http://localhost:4000 \
    cluster-list
                                  ID  Name
56ccd3cb-cb2d-40a6-a622-6a94543295e5  mycluster

$ python3 main.py --url http://localhost:4000 \
    cluster-list --cluster-id 56ccd3cb-cb2d-40a6-a622-6a94543295e5
                                  ID  Name
56ccd3cb-cb2d-40a6-a622-6a94543295e5  mycluster
```

## Cluster Remove

```
$ python3 main.py --url http://localhost:4000 \
    cluster-remove \
    --cluster-id 56ccd3cb-cb2d-40a6-a622-6a94543295e5
Cluster deleted successfully
```

## Node Add to Cluster

```
$ python3 main.py --url http://localhost:4000 \
    node-add node1.example \
    --cluster-id 56ccd3cb-cb2d-40a6-a622-6a94543295e5
Node added to Cluster successfully
Node ID: 875053c5-fe54-40da-8229-3ae99df93171
```

## Node Update

```
$ python3 main.py --url http://localhost:4000 \
    node-update node1.example.com \
    --cluster-id 56ccd3cb-cb2d-40a6-a622-6a94543295e5 \
    --node-id 875053c5-fe54-40da-8229-3ae99df93171
Node details updated successfully
```

## Node List

```
$ python3 main.py --url http://localhost:4000 \
    node-list \
    --cluster-id 56ccd3cb-cb2d-40a6-a622-6a94543295e5
                                  ID  Hostname
875053c5-fe54-40da-8229-3ae99df93171  node1.example.com
    
$ python3 main.py --url http://localhost:4000 \
    node-list \
    --cluster-id 56ccd3cb-cb2d-40a6-a622-6a94543295e5
    --node-id 875053c5-fe54-40da-8229-3ae99df93171
                                  ID  Hostname
875053c5-fe54-40da-8229-3ae99df93171  node1.example.com
```

## Node Remove

```
$ python3 main.py --url http://localhost:4000 \
    node-remove \
    --cluster-id 56ccd3cb-cb2d-40a6-a622-6a94543295e5 \
    --node-id 875053c5-fe54-40da-8229-3ae99df93171
Node deleted successfully
```

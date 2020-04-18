# Moana

## Development Setup

```
$ wget https://packages.erlang-solutions.com/erlang-solutions_2.0_all.deb && sudo dpkg -i erlang-solutions_2.0_all.deb
$ sudo apt-get update
$ sudo apt-get -y install esl-erlang elixir postgresql
$ mix local.hex --force
$ mix local.rebar --force
```

Install project dependencies

```
$ cd moana
$ mix deps.get
```

Database setup

```
sudo su - postgres
$ psql
postgres-# CREATE DATABSE moana_dev
postgres-# CREATE USER postgres;
postgres-# ALTER USER postgres PASSWORD 'postgres';
postgres-# ALTER USER postgres WITH SUPERUSER;
```

Database Migrations

```
$ mix ecto.create
$ mix ecto.migrate
```

Start Server

```
$ mix phx.server
```

Now you can visit [`localhost:4000`](http://localhost:4000) from your browser.


## CLI

Create a Cluster using,

```
$ cd cli
$ python3 -m moana.main cluster create mycluster
Cluster created successfully
Cluster ID: 7253f57e-3d7f-4fe0-a970-63cbd62dbe56
```

Register a node using,

```
$ python3 -m moana.main node join node1.example.com -c mycluster
Node added to Cluster successfully
Node ID: a940d1a8-562c-4b1e-8da8-cf662a671112
```

Now initiate Create Volume Request,

```
$ python3 -m moana.main volume create gvol1 node1.example.com:/bricks/b1 -c mycluster
Volume creation request sent
Task ID: 52d4b435-9cf6-4d6d-89ea-1794f7154c74
```

Check the status of the task using,

```
$ python3 -m moana.main task list
```

or

```
$ python3 -m moana.main task list           \
    -t 52d4b435-9cf6-4d6d-89ea-1794f7154c74 \
    -c mycluster
```

Once node agent updates the status as Success/Failure, then Volume
list will show the Volume details.

```
$ python3 -m moana.main volume list -c mycluster
```

## Node Agent

Usage and developer Contributing details are documented [here](node_agent/README.md)


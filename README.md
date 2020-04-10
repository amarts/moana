# Moana

## Initial Setup

### Project Create

```
$ mix phx.new moana --no-webpack --no-html
Fetch and install dependencies? [Yn] y
* running mix deps.get
* running mix deps.compile

We are almost there! The following steps are missing:

    $ cd moana

Then configure your database in config/dev.exs and run:

    $ mix ecto.create

Start your Phoenix app with:

    $ mix phx.server

You can also run your app inside IEx (Interactive Elixir) as:

    $ iex -S mix phx.server

```

### Create Git repo and initial commit

```
$ cd moana
$ git init
$ git config user.name <Your Name>
$ git config user.email <Your Email>
$ git add .
$ git commit -s
```

## Database setup(Development)

```
$ psql
CREATE USER postgres;
ALTER USER postgres PASSWORD 'postgres';
ALTER USER postgres WITH SUPERUSER;
```

## Tables Setup

```
mix phx.gen.json Accounts Cluster clusters name:string
```

Update the `unique_constraint` as required. and then run `ecto.migrate`


## Start Phoenix Server

* Install dependencies with `mix deps.get`
* Create and migrate your database with `mix ecto.setup`
* Start Phoenix endpoint with `mix phx.server`

Now you can visit [`localhost:4000`](http://localhost:4000) from your browser.

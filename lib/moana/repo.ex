defmodule Moana.Repo do
  use Ecto.Repo,
    otp_app: :moana,
    adapter: Ecto.Adapters.Postgres
end

defmodule MoanaWeb.Router do
  use MoanaWeb, :router

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/api", MoanaWeb do
    pipe_through :api
  end
end

defmodule MoanaWeb.Router do
  use MoanaWeb, :router

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/api/v1", MoanaWeb do
    pipe_through :api

    resources "/clusters", ClusterController, except: [:new, :edit]
  end
end

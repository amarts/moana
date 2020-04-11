defmodule MoanaWeb.Router do
  use MoanaWeb, :router

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/api/v1", MoanaWeb do
    pipe_through :api

    resources "/clusters", ClusterController, except: [:new, :edit] do
      resources "/nodes", NodeController, except: [:new, :edit]
      resources "/tasks", TaskController, except: [:new, :edit, :create]
      resources "/volumes", VolumeController, except: [:new, :edit]
    end

    resources "/nodes/:node_id/tasks", NodeTaskController, except: [:new, :edit, :create]
  end
end

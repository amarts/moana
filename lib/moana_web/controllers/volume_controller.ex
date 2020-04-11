defmodule MoanaWeb.VolumeController do
  use MoanaWeb, :controller
  import Jason

  alias Moana.Messages
  alias Moana.Messages.Task
  alias Moana.Messages.NodeTask
  alias Moana.VolumeTasks

  action_fallback MoanaWeb.FallbackController

  def index(conn, %{"cluster_id" => cluster_id}) do
    render(conn, "index.json", volumes: [])
  end

  def create(conn, %{"volume" => volume_params, "cluster_id" => cluster_id}) do
    # TODO: Duplicate Volume check
    node_ids = VolumeTasks.get_nodes(:volume_create, volume_params)

    # TODO: Handle error
    {:ok, encoded} = Jason.encode(volume_params)

    task_params = %{
      state: "Creating",
      cluster_id: cluster_id,
      type: "VOLUME_CREATE",
      data: encoded
    }
    IO.inspect node_ids
    with {:ok, %Task{} = task} <- Messages.create_task(task_params) do
      # TODO: Handle error while adding node tasks
      Enum.map(node_ids, fn node_id ->
        Messages.create_node_task(
          %{
            state: "Pending",
            task_id: task.id,
            node_id: node_id
          }
        )
      end)

      conn
      |> put_status(:created)
      |> put_resp_header("location", Routes.cluster_task_path(conn, :show, cluster_id, task))
      |> render(MoanaWeb.TaskView, "showid.json", task: task)
    end
  end

  def show(conn, %{"id" => id}) do
    render(conn, "show.json", volume: %{})
  end

  def update(conn, %{"id" => id, "task" => task_params}) do
    # TODO: What details can be updated?
  end

  def delete(conn, %{"id" => id}) do
    # TODO: Volume Delete request
  end
end

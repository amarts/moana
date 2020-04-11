defmodule MoanaWeb.NodeTaskController do
  use MoanaWeb, :controller

  alias Moana.Messages
  alias Moana.Messages.Task
  alias Moana.Messages.NodeTask

  action_fallback MoanaWeb.FallbackController

  def index(conn, %{"node_id" => node_id}) do
    node_tasks = Messages.list_nodetasks(node_id)
    render(conn, "index.json", node_tasks: node_tasks)
  end

  def show(conn, %{"id" => id}) do
    node_task = Messages.get_node_task!(id)
    render(conn, "show.json", node_task: node_task)
  end

  def update(conn, %{"id" => id, "task" => task_params}) do
    node_task = Messages.get_node_task!(id)

    with {:ok, %NodeTask{} = node_task} <- Messages.update_node_task(node_task, task_params) do
      render(conn, "show.json", node_task: node_task)
    end
  end

  def delete(conn, %{"id" => id}) do
    node_task = Messages.get_node_task!(id)

    with {:ok, %NodeTask{}} <- Messages.delete_node_task(node_task) do
      send_resp(conn, :no_content, "")
    end
  end
end

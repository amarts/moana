defmodule MoanaWeb.TaskController do
  use MoanaWeb, :controller

  alias Moana.Messages
  alias Moana.Messages.Task
  alias Moana.Messages.NodeTask

  action_fallback MoanaWeb.FallbackController

  def index(conn, %{"cluster_id" => cluster_id}) do
    tasks = Messages.list_tasks(cluster_id)
    render(conn, "index.json", tasks: tasks)
  end

  def show(conn, %{"id" => id}) do
    task = Messages.get_task!(id)
    render(conn, "show.json", task: task)
  end

  def update(conn, %{"id" => id, "task" => task_params}) do
    task = Messages.get_task!(id)

    with {:ok, %Task{} = task} <- Messages.update_task(task, task_params) do
      render(conn, "show.json", task: task)
    end
  end

  def delete(conn, %{"id" => id}) do
    task = Messages.get_task!(id)

    with {:ok, %Task{}} <- Messages.delete_task(task) do
      send_resp(conn, :no_content, "")
    end
  end
end

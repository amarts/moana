defmodule MoanaWeb.NodeTaskView do
  use MoanaWeb, :view
  alias MoanaWeb.NodeTaskView

  def render("index.json", %{node_tasks: node_tasks}) do
    %{data: render_many(node_tasks, NodeTaskView, "nodetask.json")}
  end

  def render("show.json", %{node_task: node_task}) do
    %{data: render_one(node_task, NodeTaskView, "nodetask.json")}
  end

  def render("nodetask.json", %{node_task: node_task}) do
    %{id: node_task.id,
      state: node_task.state,
      task: render_one(node_task.tasks, NodeTaskView, "task.json", as: :task),
      node_id: node_task.node_id
    }
  end

  def render("task.json", %{task: task}) do
    %{
      id: task.id,
      state: task.state,
      data: task.data,
      type: task.type
    }
  end
end

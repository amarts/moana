defmodule MoanaWeb.TaskView do
  use MoanaWeb, :view
  alias MoanaWeb.TaskView

  def render("index.json", %{tasks: tasks}) do
    %{data: render_many(tasks, TaskView, "task.json")}
  end

  def render("show.json", %{task: task}) do
    %{data: render_one(task, TaskView, "task.json")}
  end

  def render("showid.json", %{task: task}) do
    %{
      data: %{id: task.id}
    }
  end

  def render("task.json", %{task: task}) do
    %{id: task.id,
      state: task.state,
      type: task.type,
      nodetasks: render_many(task.nodetasks, TaskView, "nodetask.json", as: :nodetask),
      data: task.data
    }
  end

  def render("nodetask.json", %{nodetask: nodetask}) do
    %{
      id: nodetask.id,
      state: nodetask.state,
      node: render_one(nodetask.nodes, TaskView, "node.json", as: :node)
    }
  end

  def render("node.json", %{node: node}) do
    %{
      id: node.id,
      hostname: node.hostname
    }
  end
end

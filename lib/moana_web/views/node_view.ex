defmodule MoanaWeb.NodeView do
  use MoanaWeb, :view
  alias MoanaWeb.NodeView

  def render("index.json", %{nodes: nodes}) do
    %{data: render_many(nodes, NodeView, "node.json")}
  end

  def render("show.json", %{node: node}) do
    %{data: render_one(node, NodeView, "node.json")}
  end

  def render("node.json", %{node: node}) do
    %{id: node.id,
      hostname: node.hostname}
  end
end

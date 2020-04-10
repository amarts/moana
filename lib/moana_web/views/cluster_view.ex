defmodule MoanaWeb.ClusterView do
  use MoanaWeb, :view
  alias MoanaWeb.ClusterView

  def render("index.json", %{clusters: clusters}) do
    %{data: render_many(clusters, ClusterView, "cluster.json")}
  end

  def render("show.json", %{cluster: cluster}) do
    %{data: render_one(cluster, ClusterView, "cluster.json")}
  end

  def render("cluster.json", %{cluster: cluster}) do
    %{id: cluster.id,
      name: cluster.name}
  end
end

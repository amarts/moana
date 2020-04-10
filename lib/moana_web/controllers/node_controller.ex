defmodule MoanaWeb.NodeController do
  use MoanaWeb, :controller

  alias Moana.Storage
  alias Moana.Storage.Node

  action_fallback MoanaWeb.FallbackController

  def index(conn, %{"cluster_id" => cluster_id}) do
    nodes = Storage.list_nodes(cluster_id)
    render(conn, "index.json", nodes: nodes)
  end

  def create(conn, %{"node" => node_params, "cluster_id" => cluster_id}) do
    with {:ok, %Node{} = node} <- Storage.create_node(Map.put(node_params, "cluster_id", cluster_id)) do
      conn
      |> put_status(:created)
      |> put_resp_header("location", Routes.cluster_node_path(conn, :show, cluster_id, node))
      |> render("show.json", node: node)
    end
  end

  def show(conn, %{"id" => id}) do
    node = Storage.get_node!(id)
    render(conn, "show.json", node: node)
  end

  def update(conn, %{"id" => id, "node" => node_params}) do
    node = Storage.get_node!(id)

    with {:ok, %Node{} = node} <- Storage.update_node(node, node_params) do
      render(conn, "show.json", node: node)
    end
  end

  def delete(conn, %{"id" => id}) do
    node = Storage.get_node!(id)

    with {:ok, %Node{}} <- Storage.delete_node(node) do
      send_resp(conn, :no_content, "")
    end
  end
end

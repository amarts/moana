defmodule MoanaWeb.ClusterController do
  use MoanaWeb, :controller

  alias Moana.Storage
  alias Moana.Storage.Cluster

  action_fallback MoanaWeb.FallbackController

  def index(conn, _params) do
    clusters = Storage.list_clusters()
    render(conn, "index.json", clusters: clusters)
  end

  def create(conn, %{"cluster" => cluster_params}) do
    with {:ok, %Cluster{} = cluster} <- Storage.create_cluster(cluster_params) do
      conn
      |> put_status(:created)
      |> put_resp_header("location", Routes.cluster_path(conn, :show, cluster))
      |> render("show.json", cluster: Map.put(cluster, :nodes, []))
    end
  end

  def show(conn, %{"id" => id}) do
    cluster = Storage.get_cluster!(id)
    render(conn, "show.json", cluster: cluster)
  end

  def update(conn, %{"id" => id, "cluster" => cluster_params}) do
    cluster = Storage.get_cluster!(id)

    with {:ok, %Cluster{} = cluster} <- Storage.update_cluster(cluster, cluster_params) do
      render(conn, "show.json", cluster: cluster)
    end
  end

  def delete(conn, %{"id" => id}) do
    cluster = Storage.get_cluster!(id)

    with {:ok, %Cluster{}} <- Storage.delete_cluster(cluster) do
      send_resp(conn, :no_content, "")
    end
  end
end

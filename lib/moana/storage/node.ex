defmodule Moana.Storage.Node do
  use Ecto.Schema
  import Ecto.Changeset

  @primary_key {:id, :binary_id, autogenerate: true}
  @foreign_key_type :binary_id
  schema "nodes" do
    field :hostname, :string
    belongs_to :clusters, Moana.Storage.Cluster, [foreign_key: :cluster_id]
    has_many :nodetasks, Moana.Messages.NodeTask, foreign_key: :node_id

    timestamps()
  end

  @doc false
  def changeset(node, attrs) do
    node
    |> cast(attrs, [:hostname, :cluster_id])
    |> validate_required([:hostname, :cluster_id])
    |> foreign_key_constraint(:cluster_id)
    |> foreign_key_constraint(:node_id)
    |> unique_constraint(:hostname, name: :nodes_hostname_cluster_id_index)
  end
end

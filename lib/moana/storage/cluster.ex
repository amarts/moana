defmodule Moana.Storage.Cluster do
  use Ecto.Schema
  import Ecto.Changeset

  @primary_key {:id, :binary_id, autogenerate: true}
  @foreign_key_type :binary_id
  schema "clusters" do
    field :name, :string
    has_many :nodes, Moana.Storage.Node, foreign_key: :cluster_id
    has_many :tasks, Moana.Messages.Task, foreign_key: :cluster_id
    has_many :volumes, Moana.Storage.Volume, foreign_key: :cluster_id

    timestamps()
  end

  @doc false
  def changeset(cluster, attrs) do
    cluster
    |> cast(attrs, [:name])
    |> validate_required([:name])
    |> unique_constraint(:name)
    |> foreign_key_constraint(:cluster_id)
  end
end

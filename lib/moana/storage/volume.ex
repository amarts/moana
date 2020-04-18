defmodule Moana.Storage.Volume do
  use Ecto.Schema
  import Ecto.Changeset

  @primary_key {:id, :binary_id, autogenerate: true}
  @foreign_key_type :binary_id
  schema "volumes" do
    field :name, :string
    field :state, :string
    field :type, :string
    belongs_to :clusters, Moana.Storage.Cluster, [foreign_key: :cluster_id]

    timestamps()
  end

  @doc false
  def changeset(volume, attrs) do
    volume
    |> cast(attrs, [:name, :state, :type, :cluster_id])
    |> validate_required([:name, :state, :type, :cluster_id])
    |> foreign_key_constraint(:cluster_id)
    |> unique_constraint(:name, name: :volumes_name_cluster_id_index)
  end
end

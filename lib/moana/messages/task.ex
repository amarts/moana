defmodule Moana.Messages.Task do
  use Ecto.Schema
  import Ecto.Changeset

  @primary_key {:id, :binary_id, autogenerate: true}
  @foreign_key_type :binary_id
  schema "tasks" do
    field :data, :string
    field :state, :string
    field :type, :string
    has_many :nodetasks, Moana.Messages.NodeTask, foreign_key: :task_id
    belongs_to :clusters, Moana.Storage.Cluster, [foreign_key: :cluster_id]

    timestamps()
  end

  @doc false
  def changeset(task, attrs) do
    task
    |> cast(attrs, [:type, :data, :state, :cluster_id])
    |> validate_required([:type, :data, :state, :cluster_id])
    |> foreign_key_constraint(:task_id)
    |> foreign_key_constraint(:cluster_id)
  end
end

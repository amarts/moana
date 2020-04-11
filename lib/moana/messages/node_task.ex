defmodule Moana.Messages.NodeTask do
  use Ecto.Schema
  import Ecto.Changeset

  @primary_key {:id, :binary_id, autogenerate: true}
  @foreign_key_type :binary_id
  schema "nodetasks" do
    field :response, :string
    field :state, :string
    belongs_to :tasks, Moana.Messages.Task, [foreign_key: :task_id]
    belongs_to :nodes, Moana.Storage.Node, [foreign_key: :node_id]

    timestamps()
  end

  @doc false
  def changeset(node_task, attrs) do
    node_task
    |> cast(attrs, [:response, :state, :task_id, :node_id])
    |> validate_required([:state, :task_id, :node_id])
    |> foreign_key_constraint(:task_id)
    |> foreign_key_constraint(:node_id)
  end
end

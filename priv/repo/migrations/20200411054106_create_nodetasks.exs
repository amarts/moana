defmodule Moana.Repo.Migrations.CreateNodetasks do
  use Ecto.Migration

  def change do
    create table(:nodetasks, primary_key: false) do
      add :id, :binary_id, primary_key: true
      add :response, :string
      add :state, :string
      add :task_id, references(:tasks, on_delete: :nothing, type: :binary_id)
      add :node_id, references(:nodes, on_delete: :nothing, type: :binary_id)

      timestamps()
    end

    create index(:nodetasks, [:task_id])
    create index(:nodetasks, [:node_id])
  end
end

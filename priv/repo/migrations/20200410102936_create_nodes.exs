defmodule Moana.Repo.Migrations.CreateNodes do
  use Ecto.Migration

  def change do
    create table(:nodes, primary_key: false) do
      add :id, :binary_id, primary_key: true
      add :hostname, :string
      add :cluster_id, references(:clusters, on_delete: :nothing, type: :binary_id)

      timestamps()
    end

    create index(:nodes, [:cluster_id])
    create unique_index(:nodes, [:hostname, :cluster_id])
  end
end

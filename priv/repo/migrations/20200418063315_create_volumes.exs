defmodule Moana.Repo.Migrations.CreateVolumes do
  use Ecto.Migration

  def change do
    create table(:volumes, primary_key: false) do
      add :id, :binary_id, primary_key: true
      add :name, :string
      add :state, :string
      add :type, :string
      add :cluster_id, references(:clusters, on_delete: :nothing, type: :binary_id)

      timestamps()
    end

    create index(:volumes, [:cluster_id])
    create unique_index(:volumes, [:name, :cluster_id])
  end
end

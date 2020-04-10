defmodule Moana.Repo.Migrations.CreateClusters do
  use Ecto.Migration

  def change do
    create table(:clusters, primary_key: false) do
      add :id, :binary_id, primary_key: true
      add :name, :string

      timestamps()
    end

    create unique_index(:clusters, [:name])

  end
end

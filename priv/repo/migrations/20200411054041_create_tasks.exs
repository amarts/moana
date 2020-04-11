defmodule Moana.Repo.Migrations.CreateTasks do
  use Ecto.Migration

  def change do
    create table(:tasks, primary_key: false) do
      add :id, :binary_id, primary_key: true
      add :type, :string
      add :data, :string
      add :state, :string
      add :cluster_id, references(:clusters, on_delete: :nothing, type: :binary_id)

      timestamps()
    end

  end
end

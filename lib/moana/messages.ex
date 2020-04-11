defmodule Moana.Messages do
  @moduledoc """
  The Messages context.
  """

  import Ecto.Query, warn: false
  alias Moana.Repo

  alias Moana.Messages.Task
  alias Moana.Messages.NodeTask
  alias Moana.Storage.Node

  @doc """
  Returns the list of tasks.

  ## Examples

      iex> list_tasks()
      [%Task{}, ...]

  """
  def list_tasks do
    Repo.all(Task)
  end

  @doc """
  Returns the list of tasks.

  ## Examples

      iex> list_tasks()
      [%Task{}, ...]

  """
  def list_tasks(cluster_id) do
    Repo.all(from t in Task,
      join: nt in NodeTask, on: t.id == nt.task_id,
      join: n in Node, on: nt.node_id == n.id,
      where: t.cluster_id == ^cluster_id,
      preload: [nodetasks: {nt, nodes: n}]
    )
  end

  @doc """
  Gets a single task.

  Raises `Ecto.NoResultsError` if the Task does not exist.

  ## Examples

      iex> get_task!(123)
      %Task{}

      iex> get_task!(456)
      ** (Ecto.NoResultsError)

  """
  def get_task!(id) do
    Repo.get!(
    (
      from t in Task,
      join: nt in NodeTask, on: t.id == nt.task_id,
      join: n in Node, on: nt.node_id == n.id,
      preload: [nodetasks: {nt, nodes: n}]
    ),
      id
    )
  end

  @doc """
  Creates a task.

  ## Examples

      iex> create_task(%{field: value})
      {:ok, %Task{}}

      iex> create_task(%{field: bad_value})
      {:error, %Ecto.Changeset{}}

  """
  def create_task(attrs \\ %{}) do
    %Task{}
    |> Task.changeset(attrs)
    |> Repo.insert()
  end

  @doc """
  Updates a task.

  ## Examples

      iex> update_task(task, %{field: new_value})
      {:ok, %Task{}}

      iex> update_task(task, %{field: bad_value})
      {:error, %Ecto.Changeset{}}

  """
  def update_task(%Task{} = task, attrs) do
    task
    |> Task.changeset(attrs)
    |> Repo.update()
  end

  @doc """
  Deletes a task.

  ## Examples

      iex> delete_task(task)
      {:ok, %Task{}}

      iex> delete_task(task)
      {:error, %Ecto.Changeset{}}

  """
  def delete_task(%Task{} = task) do
    Repo.delete(task)
  end

  @doc """
  Returns an `%Ecto.Changeset{}` for tracking task changes.

  ## Examples

      iex> change_task(task)
      %Ecto.Changeset{source: %Task{}}

  """
  def change_task(%Task{} = task) do
    Task.changeset(task, %{})
  end

  @doc """
  Returns the list of nodetasks.

  ## Examples

      iex> list_nodetasks()
      [%NodeTask{}, ...]

  """
  def list_nodetasks(node_id) do
    Repo.all(from nt in NodeTask,
      join: t in Task, on: t.id == nt.task_id,
      where: nt.node_id == ^node_id,
      preload: [:tasks]
    )
  end

  @doc """
  Gets a single node_task.

  Raises `Ecto.NoResultsError` if the Node task does not exist.

  ## Examples

      iex> get_node_task!(123)
      %NodeTask{}

      iex> get_node_task!(456)
      ** (Ecto.NoResultsError)

  """
  def get_node_task!(id) do
    Repo.get!(
    (
      from nt in NodeTask,
      join: t in Task, on: t.id == nt.task_id,
      preload: [:tasks]
    ),
      id)
  end

  @doc """
  Creates a node_task.

  ## Examples

      iex> create_node_task(%{field: value})
      {:ok, %NodeTask{}}

      iex> create_node_task(%{field: bad_value})
      {:error, %Ecto.Changeset{}}

  """
  def create_node_task(attrs \\ %{}) do
    %NodeTask{}
    |> NodeTask.changeset(attrs)
    |> Repo.insert()
  end

  @doc """
  Updates a node_task.

  ## Examples

      iex> update_node_task(node_task, %{field: new_value})
      {:ok, %NodeTask{}}

      iex> update_node_task(node_task, %{field: bad_value})
      {:error, %Ecto.Changeset{}}

  """
  def update_node_task(%NodeTask{} = node_task, attrs) do
    node_task
    |> NodeTask.changeset(attrs)
    |> Repo.update()
  end

  @doc """
  Deletes a node_task.

  ## Examples

      iex> delete_node_task(node_task)
      {:ok, %NodeTask{}}

      iex> delete_node_task(node_task)
      {:error, %Ecto.Changeset{}}

  """
  def delete_node_task(%NodeTask{} = node_task) do
    Repo.delete(node_task)
  end

  @doc """
  Returns an `%Ecto.Changeset{}` for tracking node_task changes.

  ## Examples

      iex> change_node_task(node_task)
      %Ecto.Changeset{source: %NodeTask{}}

  """
  def change_node_task(%NodeTask{} = node_task) do
    NodeTask.changeset(node_task, %{})
  end
end

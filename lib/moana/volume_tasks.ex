defmodule Moana.VolumeTasks do
  alias Moana.Messages
  alias Moana.Storage

  def valid(:volume_create, params) do
    # TODO: Duplicate Volume check by checking in volumes table(within cluster)
    # TODO: Duplicate Volname in in-progress task list(within cluster)
    # TODO: Number of bricks validation based on Volume Type
    # TODO: Best Practice validation
    # TODO: Brick Path in node is already part of other Volumes
    true
  end

  def get_nodes(:volume_create, params) do
    Enum.map(Map.fetch!(params, "bricks"), fn brick ->
      Map.fetch!(brick, "node_id")
    end)
  end

  def all_node_tasks_complete(task) do
    completed_tasks = Enum.filter(task.nodetasks, fn nodetask ->
      nodetask.state == "Success" || nodetask.state == "Failure"
    end)
    length(completed_tasks) == length(task.nodetasks)
  end

  def aggregated_task_state(task) do
    success_tasks = Enum.filter(task.nodetasks, fn nodetask ->
      nodetask.state == "Success"
    end)
    if length(task.nodetasks) == length(success_tasks) do
      "Success"
    else
      "Failure"
    end
  end

  def on_success(:volume_create, task) do
    {:ok, decoded} = Jason.decode(task.data)
    Storage.create_volume(
      %{
        name: Map.get(decoded, "name"),
        state: "Created",
        cluster_id: task.cluster_id,
        type: "Distribute"
      }
    )
    # TODO: Insert to subvols and bricks table
  end
end

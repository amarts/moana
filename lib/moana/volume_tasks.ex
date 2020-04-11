defmodule Moana.VolumeTasks do

  def valid(:volume_create, params) do
    # TODO: Validate each argument for Volume Create Request
    true
  end

  def get_nodes(:volume_create, params) do
    Enum.map(Map.fetch!(params, "bricks"), fn brick ->
      Map.fetch!(brick, "node_id")
    end)
  end

  def on_success(:volume_create, params) do
    # TODO: Insert to Volumes, subvols and bricks table
  end
end

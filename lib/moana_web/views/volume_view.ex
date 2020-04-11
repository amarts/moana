defmodule MoanaWeb.VolumeView do
  use MoanaWeb, :view
  alias MoanaWeb.VolumeView

  def render("index.json", %{volumes: volumes}) do
    %{data: render_many(volumes, VolumeView, "volume.json")}
  end

  def render("show.json", %{volume: volume}) do
    %{data: render_one(volume, VolumeView, "volume.json")}
  end

  def render("volume.json", %{volume: volume}) do
    %{id: volume.id,
      name: volume.name}
  end
end

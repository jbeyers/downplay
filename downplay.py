import click
import os
from pytube import Playlist


@click.command()
@click.option(
    "--playlist",
    default="",
    prompt="Playlist link",
    help="The playlist you want to download",
)
@click.option("--target", prompt="Target dir", help="The target directory")
def download(playlist, target):
    pl = Playlist(playlist)
    full_target = "downloads/" + target
    if not os.path.exists(full_target):
        os.makedirs(full_target)
    pl.download_all(full_target)


if __name__ == "__main__":
    download()

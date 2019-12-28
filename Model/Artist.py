# <editor-fold desc="Libaries">
from typing import *
# </editor-fold>

# <editor-fold desc="Model">
from Model.MusicTag import MusicTag
# </editor-fold>


class Artist:

    # <editor-fold desc="Constructor">
    def __init__(self, input_data: dict):
        self.name: str = input_data["name"]
        self.lastfm_url: str = input_data["url"]
        self.lastfm_listeners: str = input_data["stats"]["listeners"]
        self.lastfm_playcount: str = input_data["stats"]["playcount"]
        self.image: str = list(
            filter(
                lambda image: image["size"] == "extralarge",
                input_data["image"]
            )
        )[0]["#text"]
        self.toptags: List[MusicTag] = list(
            map(
                lambda tag: MusicTag(input_data=tag),
                input_data["tags"]["tag"]
            )
        )
    # </editor-fold>

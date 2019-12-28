# <editor-fold desc="Libaries">
from typing import *
# </editor-fold>

# <editor-fold desc="Model">
from Model.MusicTag import MusicTag
# </editor-fold>


class Track:

    # <editor-fold desc="Description">
    def __init__(self, input_data: dict):
        self.name: str = input_data["name"]
        self.lastfm_url: str = input_data["url"]
        self.lastfm_listeners: str = input_data["listeners"]
        self.lastfm_playcount: str = input_data["playcount"]
        self.artist: str = input_data["artist"]["name"]
        self.toptags: List[MusicTag] = list(
            map(
                lambda tag: MusicTag(input_data=tag),
                input_data["toptags"]["tag"]
            )
        )
    # </editor-fold>

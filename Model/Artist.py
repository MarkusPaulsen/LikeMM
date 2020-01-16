# <editor-fold desc="Libaries">
from typing import *
# </editor-fold>

# <editor-fold desc="Model">
from Model.MusicTag import MusicTag
# </editor-fold>


class Artist:

    # <editor-fold desc="Constructor">
    def __init__(self, lastfm_input: dict, spotify_input: dict):
        self.name: str = lastfm_input["name"]

        self.lastfm_url: str = lastfm_input["url"]
        self.spotify_url: str = spotify_input["external_urls"]["spotify"]
        self.spotify_uri: str = spotify_input["uri"]
        self.spotify_image: str = spotify_input["images"][0]["url"]

        self.lastfm_listeners: str = lastfm_input["stats"]["listeners"]
        self.lastfm_playcount: str = lastfm_input["stats"]["playcount"]
        self.lastfm_tags: List[MusicTag] = list(
            map(
                lambda tag: MusicTag(lastfm_input=tag),
                lastfm_input["tags"]["tag"]
            )
        )
        self.spotify_popularity: int = spotify_input["popularity"]
        self.spotify_followers: int = spotify_input["followers"]["total"]
        self.spotify_genres: List[str] = spotify_input["genres"]

    def json(self):
        return {
            "name": self.name,

            "lastfm_url": self.lastfm_url,
            "spotify_url": self.spotify_url,
            "spotify_uri": self.spotify_uri,
            "spotify_image": self.spotify_image,

            "lastfm_listeners": self.lastfm_listeners,
            "lastfm_playcount": self.lastfm_playcount,
            "lastfm_tags": list(map(lambda tag: tag.json(), self.lastfm_tags)),
            "spotify_popularity": self.spotify_popularity,
            "spotify_followers": self.spotify_followers,
            "spotify_genres": self.spotify_genres
        }
    # </editor-fold>

# <editor-fold desc="Libaries">
from typing import *
# </editor-fold>

# <editor-fold desc="Model">
from Model.MusicTag import MusicTag
# </editor-fold>


class Track:

    # <editor-fold desc="Description">
    def __init__(self, lastfm_input: dict, spotify_input: dict, billboard_input: dict):
        self.name: str = lastfm_input["name"]
        self.artist: str = lastfm_input["artist"]["name"]

        self.lastfm_duration_ms: int = lastfm_input["duration"]
        self.spotify_duration_ms: int = spotify_input["duration_ms"]
        self.spotify_explicit: bool = spotify_input["explicit"]
        self.spotify_acousticness: float = spotify_input["acousticness"]
        self.spotify_danceability: float = spotify_input["danceability"]
        self.spotify_energy: float = spotify_input["energy"]
        self.spotify_instrumentalness: float = spotify_input["instrumentalness"]
        self.spotify_liveness: float = spotify_input["liveness"]
        self.spotify_loudness: float = spotify_input["loudness"]
        self.spotify_speechiness: float = spotify_input["speechiness"]
        self.spotify_valence: float = spotify_input["valence"]
        self.spotify_tempo: float = spotify_input["tempo"]

        self.lastfm_url: str = lastfm_input["url"]
        self.spotify_url: str = spotify_input["external_urls"]["spotify"]
        self.spotify_preview_url: str = spotify_input["preview_url"]
        self.spotify_uri: str = spotify_input["uri"]

        self.lastfm_listeners: str = lastfm_input["listeners"]
        self.lastfm_playcount: str = lastfm_input["playcount"]
        self.lastfm_tags: List[MusicTag] = list(
            map(
                lambda tag: MusicTag(lastfm_input=tag),
                lastfm_input["toptags"]["tag"]
            )
        )
        self.spotify_popularity: int = spotify_input["popularity"]

    def json(self):
        return {
            "name": self.name,
            "artist": self.artist,

            "lastfm_duration_ms": self.lastfm_duration_ms,
            "spotify_duration_ms": self.spotify_duration_ms,
            "spotify_explicit": self.spotify_explicit,
            "spotify_acousticness": self.spotify_acousticness,
            "spotify_danceability": self.spotify_danceability,
            "spotify_energy": self.spotify_energy,
            "spotify_instrumentalness": self.spotify_instrumentalness,
            "spotify_liveness": self.spotify_liveness,
            "spotify_loudness": self.spotify_loudness,
            "spotify_speechiness": self.spotify_speechiness,
            "spotify_valence": self.spotify_valence,
            "spotify_tempo": self.spotify_tempo,

            "lastfm_url": self.lastfm_url,
            "spotify_url": self.spotify_url,
            "spotify_preview_url": self.spotify_preview_url,
            "spotify_uri": self.spotify_uri,

            "lastfm_listeners": self.lastfm_listeners,
            "lastfm_playcount": self.lastfm_playcount,
            "lastfm_tags": list(map(lambda tag: tag.json(), self.lastfm_tags)),
            "spotify_popularity": self.spotify_popularity
        }
    # </editor-fold>

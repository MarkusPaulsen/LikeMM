from typing import *
from APIs.MongoDBAPI import MongoDBAPI


class LastFMChartsEPController:
    def __init__(self):
        self.mongodb_api = MongoDBAPI()
        self.chart_list = []

    def load_chart_list(self):
        self.chart_list = list(self.mongodb_api.query_lastfm_db(
            selection={},
            projection={
                "name": 1,
                "artist": 1,

                "lastfm_duration_ms": 1,
                "spotify_duration_ms": 1,
                "spotify_explicit": 1,
                "spotify_acousticness": 1,
                "spotify_danceability": 1,
                "spotify_energy": 1,
                "spotify_instrumentalness": 1,
                "spotify_liveness": 1,
                "spotify_loudness": 1,
                "spotify_speechiness": 1,
                "spotify_valence": 1,
                "spotify_tempo": 1,

                "lastfm_url": 1,
                "spotify_url": 1,
                "spotify_preview_url": 1,
                "spotify_uri": 1,

                "lastfm_listeners": 1,
                "lastfm_playcount": 1,
                "lastfm_tags": 1,
                "spotify_popularity": 1
            }
        ))
        for chart in self.chart_list:
            chart.pop("_id", None)

    def json(self) -> List[dict]:
        self.load_chart_list()
        return self.chart_list

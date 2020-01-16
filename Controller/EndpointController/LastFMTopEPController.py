from typing import *
from APIs.MongoDBAPI import MongoDBAPI


class LastFMTopEPController:
    def __init__(self):
        self.mongo_db_api = MongoDBAPI()

    def json(self, nr) -> List[dict]:
        last_fm_chart_list = list(self.mongo_db_api.query_last_fm_chart_db({}, {
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
        }))
        for last_fm_chart in last_fm_chart_list:
            last_fm_chart.pop("_id", None)
        output = last_fm_chart_list[:max(int(nr), len(last_fm_chart_list))]
        return output

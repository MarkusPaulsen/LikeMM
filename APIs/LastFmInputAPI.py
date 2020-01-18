# <editor-fold desc="Libaries">
from typing import *
import os
import requests
# </editor-fold>

# <editor-fold desc="Model">
from Model.Artist import Artist
# </editor-fold>


# noinspection PyMethodMayBeStatic
class LastFmInputAPI:

    def __init__(self):
        self.lastFm_API_key: str = os.environ["lastFm_API_key"]

    # <editor-fold desc="Track input">
    def get_lastfm_input_track(self, track_name: str, track_artist: str) -> Optional[dict]:
        try:
            reply: requests.api = requests.get(
                url="http://ws.audioscrobbler.com/2.0/?"
                + "method=" + "track.getInfo"
                + "&api_key=" + self.lastFm_API_key
                + "&artist=" + track_artist
                + "&track=" + track_name
                + "&format=json")
            reply_json: dict = reply.json()
            output: dict = reply_json["track"]
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None
    # </editor-fold>

    # <editor-fold desc="Artist input">
    def get_lastfm_input_artist(self, artist_name: str) -> Optional[dict]:
        try:
            reply: requests.api = requests.get(
                url="http://ws.audioscrobbler.com/2.0/?"
                + "method=" + "artist.getInfo"
                + "&api_key=" + self.lastFm_API_key
                + "&artist=" + artist_name
                + "&format=json")
            reply_json: dict = reply.json()
            output: dict = reply_json["artist"]
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None
    # </editor-fold>

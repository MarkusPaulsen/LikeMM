from typing import *
import requests
import base64
import os
import pprint


class SpotifyInputAPI:

    def __init__(self):
        self.spotify_client_id: str = os.environ["spotify_client_id"]
        self.spotify_client_secret: str = os.environ["spotify_client_secret"]
        self.grant_type: str = "client_credentials"
        self.basic_access_token: str = ("Basic " + base64.b64encode(
            (self.spotify_client_id + ":" + self.spotify_client_secret).encode()
        ).decode())
        self.bearer_access_token: str = None

    def update_bearer_access_token(self):
        reply_bearer_access_token: requests.api = requests.post(
            "https://accounts.spotify.com/api/token",
            data={"grant_type": self.grant_type},
            headers={"Authorization": self.basic_access_token}
        )
        reply_bearer_access_token_json: dict = reply_bearer_access_token.json()
        self.bearer_access_token = "Bearer " + reply_bearer_access_token_json["access_token"]

    # <editor-fold desc="Track input">
    def get_spotify_input_track(self, track_name: str, track_artist: str) -> Optional[dict]:
        try:
            self.update_bearer_access_token()
            reply_track: requests.api = requests.get(
                url="https://api.spotify.com/v1/search?"
                + "&q=" + track_name + " " + track_artist
                + "&type=" + "track"
                + "&market=" + "DE"
                + "&limit=" + "1",
                headers={"Authorization": self.bearer_access_token}
            )
            reply_track_json: dict = reply_track.json()
            output: dict = reply_track_json["tracks"]["items"][0]
            reply_track_info = requests.get(
                "https://api.spotify.com/v1/audio-features/" + output["id"],
                headers={"Authorization": self.bearer_access_token}
            )
            reply_track_info_json: dict = reply_track_info.json()
            output.update(reply_track_info_json)
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None
    # </editor-fold>

    # <editor-fold desc="Artist input">
    def get_spotify_input_artist(self, artist_name: str) -> Optional[dict]:
        try:
            self.update_bearer_access_token()
            reply_track: requests.api = requests.get(
                url="https://api.spotify.com/v1/search?"
                + "&q=" + artist_name
                + "&type=" + "artist"
                + "&market=" + "DE"
                + "&limit=" + "1",
                headers={"Authorization": self.bearer_access_token}
            )
            reply_track_json: dict = reply_track.json()
            output: dict = reply_track_json["artists"]["items"][0]
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None
    # </editor-fold>

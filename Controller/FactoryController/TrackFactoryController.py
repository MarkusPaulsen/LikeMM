from typing import *
from APIs.LastFmInputAPI import LastFmInputAPI
from APIs.SpotifyInputAPI import SpotifyInputAPI
from APIs.BillboardInputAPI import BillboardInputAPI
from Model.Track import Track


class TrackFactoryController:

    def __init__(self):
        self.lastfm_input_api = LastFmInputAPI()
        self.spotify_input_api = SpotifyInputAPI()
        self.billboard_input_api = BillboardInputAPI()

    def create_track(self, track_name: str, track_artist: str) -> Optional[Track]:
        try:
            lastfm_input: dict = self.lastfm_input_api.get_lastfm_input_track(
                track_name=track_name,
                track_artist=track_artist
            )
            spotify_input: dict = self.spotify_input_api.get_spotify_input_track(
                track_name=track_name,
                track_artist=track_artist
            )
            billboard_input: dict = self.billboard_input_api.get_billboard_input_track(
                track_name=track_name,
                track_artist=track_artist
            )
            output: Track = Track(
                lastfm_input=lastfm_input,
                spotify_input=spotify_input,
                billboard_input=billboard_input
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def create_tracks(self, name_artist_list: List[Tuple[str, str]]) -> List[Optional[Track]]:
        output = list(map(
            lambda track: self.create_track(
                track_name=track[0],
                track_artist=track[1]
            ),
            name_artist_list
        ))
        return output

from typing import *
from APIs.LastFmInputAPI import LastFmInputAPI
from APIs.SpotifyInputAPI import SpotifyInputAPI
from Model.Artist import Artist


class ArtistFactoryController:

    def __init__(self):
        self.lastfm_input_api = LastFmInputAPI()
        self.spotify_input_api = SpotifyInputAPI()

    def create_artist(self, artist_name: str) -> Optional[Artist]:
        try:
            lastfm_input: dict = self.lastfm_input_api.get_lastfm_input_artist(
                artist_name=artist_name
            )
            spotify_input: dict = self.spotify_input_api.get_spotify_input_artist(
                artist_name=artist_name
            )
            billboard_input: dict = self.spotify_input_api.get_spotify_input_artist(
                artist_name=artist_name
            )
            output: Artist = Artist(
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

    def create_artists(self, artist_list: List[str]) -> List[Artist]:
        artists_optional_list = list(map(
            lambda artist_name: self.create_artist(
                artist_name=artist_name
            ),
            artist_list
        ))
        output = [artist for artist in artists_optional_list if artist is not None]
        return output

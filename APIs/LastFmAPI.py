# <editor-fold desc="Libaries">
from typing import *
import os
import requests
# </editor-fold>

# <editor-fold desc="Model">
from Controller.FactoryController.ArtistFactoryController import ArtistFactoryController
from Model.Track import Track
from Model.Artist import Artist
from Controller.FactoryController.TrackFactoryController import TrackFactoryController
# </editor-fold>


# noinspection PyMethodMayBeStatic
class LastFmAPI:

    def __init__(self):
        self.lastFm_API_key: str = os.environ["lastFm_API_key"]
        self.track_factory_controller: TrackFactoryController = TrackFactoryController()
        self.artist_factory_controller: ArtistFactoryController = ArtistFactoryController()

    # <editor-fold desc="Tracks">
    def get_lastfm_charts(self, nr) -> Optional[List[Optional[Track]]]:
        try:
            reply: requests.api = requests.get(
                url="http://ws.audioscrobbler.com/2.0/?"
                + "method=" + "chart.getTopTracks"
                + "&api_key=" + self.lastFm_API_key
                + "&limit=" + str(nr)
                + "&format=json")
            reply_json: dict = reply.json()
            name_artist_list: List[Tuple[str, str]] = list(map(
                lambda track: (track["name"], track["artist"]["name"]),
                reply_json["tracks"]["track"]
            ))
            output = self.track_factory_controller.create_tracks(name_artist_list)
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None
    # </editor-fold>

    # <editor-fold desc="Artists">
    def lastfm_artist_get_top_tracks(self, artist: str) -> Optional[List[Track]]:
        try:
            reply: requests.api = requests.get(
                url="http://ws.audioscrobbler.com/2.0/?"
                + "method=" + "artist.getTopTracks"
                + "&api_key=" + self.lastFm_API_key
                + "&artist=" + artist
                + "&limit=" + "3"
                + "&format=json")
            reply_json: dict = reply.json()
            reply_json_data: dict = reply_json["toptracks"]["track"]

            def track_data_to_tracks(track_data: dict, artist_inside: str):
                print(artist_inside)
                track_inside: str = track_data["name"]
                output_inside: Optional[Track] = self.track_factory_controller.create_track(
                    track_artist=artist_inside,
                    track_name=track_inside
                )
                return output_inside

            output_with_none: List[Optional[Track]] = list(
                map(
                    lambda track_data: track_data_to_tracks(
                        track_data=track_data,
                        artist_inside=artist
                    ),
                    reply_json_data
                )
            )
            output: List[Track] = list(filter(
                None,
                output_with_none
            ))
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def lastfm_artist_get_similar(self, artist: str) -> Optional[List[Artist]]:
        try:
            reply: requests.api = requests.get(
                url="http://ws.audioscrobbler.com/2.0/?"
                + "method=" + "artist.getSimilar"
                + "&api_key=" + self.lastFm_API_key
                + "&artist=" + artist
                + "&limit=" + "3"
                + "&format=json")
            reply_json: dict = reply.json()
            reply_json_data: dict = reply_json["similarartists"]["artist"]

            def artist_data_to_artists(input_data: dict):
                print(artist)
                artist_inside: str = input_data["name"]
                output_inside: Optional[Artist] = self.artist_factory_controller.create_artist(
                    artist_name=artist_inside
                )
                return output_inside

            output_with_none: List[Optional[Artist]] = list(
                map(
                    lambda artist_data: artist_data_to_artists(
                        input_data=artist_data
                    ),
                    reply_json_data
                )
            )
            output: List[Artist] = list(filter(
                None,
                output_with_none
            ))
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None
    # </editor-fold>

    # <editor-fold desc="Tags">
    def lastfm_tag_get_top_tracks(self, tag: str) -> Optional[List[Track]]:
        try:
            reply: requests.api = requests.get(
                url="http://ws.audioscrobbler.com/2.0/?"
                + "method=" + "tag.getTopTracks"
                + "&api_key=" + self.lastFm_API_key
                + "&tag=" + tag
                + "&limit=" + "1"
                + "&format=json")
            reply_json: dict = reply.json()
            reply_json_data: dict = reply_json["tracks"]["track"]

            def track_data_to_tracks(track_data: dict) -> Optional[Track]:
                print(tag)
                artist_inside: str = track_data["artist"]["name"]
                track_inside: str = track_data["name"]
                output_inside: Optional[Track] = self.track_factory_controller.create_track(
                    track_artist=artist_inside,
                    track_name=track_inside
                )
                return output_inside

            output_with_none: List[Optional[Track]] = list(
                map(
                    lambda track_data: track_data_to_tracks(
                        track_data=track_data
                    ),
                    reply_json_data)
            )
            output: List[Track] = list(filter(
                None,
                output_with_none
            ))
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None
    # </editor-fold>

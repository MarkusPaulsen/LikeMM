# <editor-fold desc="Libaries">
from typing import *
import os
import requests
# </editor-fold>

# <editor-fold desc="Model">
from Model.Track import Track
from Model.Artist import Artist
# </editor-fold>


# noinspection PyMethodMayBeStatic
class LastFmAPI:

    # <editor-fold desc="Artists">
    def lastfm_artist_get_info(self, artist: str) -> Optional[Artist]:
        try:
            reply: requests.api = requests.get(
                url="http://ws.audioscrobbler.com/2.0/?"
                + "method=" + "artist.getInfo"
                + "&api_key=" + os.environ["lastFm_API_key"]
                + "&artist=" + artist
                + "&format=json")
            reply_json: dict = reply.json()
            reply_json_data: dict = reply_json["artist"]
            output: Artist = Artist(
                input_data=reply_json_data
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def lastfm_artist_get_top_tracks(self, artist: str) -> Optional[List[Track]]:
        try:
            reply: requests.api = requests.get(
                url="http://ws.audioscrobbler.com/2.0/?"
                + "method=" + "artist.getTopTracks"
                + "&api_key=" + os.environ["lastFm_API_key"]
                + "&artist=" + artist
                + "&limit=" + "3"
                + "&format=json")
            reply_json: dict = reply.json()
            reply_json_data: dict = reply_json["toptracks"]["track"]

            def track_data_to_tracks(track_data: dict, artist_inside: str):
                print(artist_inside)
                track_inside: str = track_data["name"]
                output_inside: Optional[Track] = self.lastfm_track_get_info(
                    artist=artist_inside,
                    track=track_inside
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
                + "&api_key=" + os.environ["lastFm_API_key"]
                + "&artist=" + artist
                + "&limit=" + "3"
                + "&format=json")
            reply_json: dict = reply.json()
            reply_json_data: dict = reply_json["similarartists"]["artist"]

            def artist_data_to_artists(input_data: dict):
                print(artist)
                artist_inside: str = input_data["name"]
                output_inside: Optional[Artist] = self.lastfm_artist_get_info(
                    artist=artist_inside
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

    # <editor-fold desc="Tracks">
    def lastfm_track_get_info(self, artist: str, track: str) -> Optional[Track]:
        try:
            reply: requests.api = requests.get(
                url="http://ws.audioscrobbler.com/2.0/?"
                + "method=" + "track.getInfo"
                + "&api_key=" + os.environ["lastFm_API_key"]
                + "&artist=" + artist
                + "&track=" + track
                + "&format=json")
            reply_json: dict = reply.json()
            reply_json_data: dict = reply_json["track"]
            output: Track = Track(input_data=reply_json_data)
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def lastfm_chart_get_top_tracks(self) -> Optional[List[Track]]:
        try:
            reply: requests.api = requests.get(
                url="http://ws.audioscrobbler.com/2.0/?"
                + "method=" + "chart.getTopTracks"
                + "&api_key=" + os.environ["lastFm_API_key"]
                + "&limit=" + "10"
                + "&format=json")
            reply_json: dict = reply.json()
            reply_json_data: dict = reply_json["tracks"]["track"]

            def track_data_to_tracks(track_data: dict) -> Optional[Track]:
                artist_inside: str = track_data["artist"]["name"]
                track_inside: str = track_data["name"]
                output_inside: Optional[Track] = self.lastfm_track_get_info(
                    artist=artist_inside,
                    track=track_inside
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

    # <editor-fold desc="Tags">
    def lastfm_tag_get_top_tracks(self, tag: str) -> Optional[List[Track]]:
        try:
            reply: requests.api = requests.get(
                url="http://ws.audioscrobbler.com/2.0/?"
                + "method=" + "tag.getTopTracks"
                + "&api_key=" + os.environ["lastFm_API_key"]
                + "&tag=" + tag
                + "&limit=" + "1"
                + "&format=json")
            reply_json: dict = reply.json()
            reply_json_data: dict = reply_json["tracks"]["track"]

            def track_data_to_tracks(track_data: dict) -> Optional[Track]:
                print(tag)
                artist_inside: str = track_data["artist"]["name"]
                track_inside: str = track_data["name"]
                output_inside: Optional[Track] = self.lastfm_track_get_info(
                    artist=artist_inside,
                    track=track_inside
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

# <editor-fold desc="Libaries">
from typing import *
import os
import requests
# </editor-fold>
# <editor-fold desc="Model">
from Model.Track import Track
# </editor-fold>
# <editor-fold desc="Controller">
from Controller.FactoryController.TrackFactoryController import TrackFactoryController
# </editor-fold>


# noinspection PyMethodMayBeStatic
class LastFmAPI:

    def __init__(self):
        self.lastFm_API_key: str = os.environ["lastfm_api_key"]
        self.track_factory_controller: TrackFactoryController = TrackFactoryController()

    # <editor-fold desc="Tracks">
    def get_lastfm_charts(self, nr) -> Optional[List[Track]]:
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

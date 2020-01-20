# <editor-fold desc="Libaries">
from typing import *
import os
import requests
# </editor-fold>


# noinspection PyMethodMayBeStatic
class OMDBInputAPI:

    def __init__(self):
        self.omdb_API_key: str = os.environ["omdb_api_key"]

    # <editor-fold desc="Track input">
    def get_themoviedb_input_movie(self, movie_name: str) -> Optional[dict]:
        try:
            reply: requests.api = requests.get(
                url="http://www.omdbapi.com/?"
                    + "apikey=" + self.omdb_API_key
                    + "&t=" + movie_name)
            reply_json: dict = reply.json()
            return reply_json
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None
    # </editor-fold>

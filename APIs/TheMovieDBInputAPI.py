# <editor-fold desc="Libaries">
from typing import *
import os
import requests
# </editor-fold>


# noinspection PyMethodMayBeStatic
class TheMovieDBInputAPI:

    def __init__(self):
        self.themoviedb_API_key: str = os.environ["themoviedb_api_key"]

    # <editor-fold desc="Track input">
    def get_themoviedb_movie_id(self, movie_name: str) -> Optional[int]:
        try:
            reply: requests.api = requests.get(
                url="https://api.themoviedb.org/3/search/movie?"
                + "api_key=" + self.themoviedb_API_key
                + "&query=" + movie_name
                + "&include_adult=" + str(True))
            reply_json: dict = reply.json()
            if len(reply_json["results"]) > 0:
                movie_id: int = reply_json["results"][0]["id"]
                return movie_id
            else:
                return None
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def get_themoviedb_movie_details(self, movie_id: int) -> Optional[dict]:
        try:
            reply: requests.api = requests.get(
                url="https://api.themoviedb.org/3/movie/" + str(movie_id) + "?"
                    + "api_key=" + self.themoviedb_API_key)
            reply_json: dict = reply.json()
            return reply_json
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def get_themoviedb_input_movie(self, movie_name: str) -> Optional[dict]:
        movie_id: Optional[int] = self.get_themoviedb_movie_id(movie_name)
        if movie_id is not None:
            movie_details: Optional[dict] = self.get_themoviedb_movie_details(movie_id)
            return movie_details
        else:
            return None
    # </editor-fold>

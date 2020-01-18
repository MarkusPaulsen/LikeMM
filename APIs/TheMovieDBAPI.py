# <editor-fold desc="Libaries">
from typing import *
import os
import requests
# </editor-fold>
# <editor-fold desc="Model">
from Model.Movie import Movie
# </editor-fold>
# <editor-fold desc="Controller">
from Controller.FactoryController.MovieFactoryController import MovieFactoryController
# </editor-fold>


# noinspection PyMethodMayBeStatic
class TheMovieDBAPI:

    def __init__(self):
        self.theMovieDB_API_key: str = os.environ["theMovieDB_API_key"]
        self.movie_factory_controller: MovieFactoryController = MovieFactoryController()

    # <editor-fold desc="Tracks">
    def get_themoviedb_charts(self, nr) -> Optional[List[Movie]]:
        try:
            reply: requests.api = requests.get(
                url="https://api.themoviedb.org/3/trending/movie/day?"
                + "api_key=" + self.theMovieDB_API_key)
            reply_json: dict = reply.json()
            movie_list_all: List[dict] = reply_json["results"]
            movie_list: List[dict] = movie_list_all[:max(len(movie_list_all), nr)]
            movie_id_list: List[int] = list(map(
                lambda movie: movie["id"],
                movie_list
            ))
            output = self.movie_factory_controller.create_movies_id(
                movie_id_list=movie_id_list
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None
    # </editor-fold>

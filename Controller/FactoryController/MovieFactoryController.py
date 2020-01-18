from typing import *
from APIs.TheMovieDBInputAPI import TheMovieDBInputAPI
from Model.Movie import Movie


class MovieFactoryController:

    def __init__(self):
        self.themoviedb_input_api = TheMovieDBInputAPI()

    def create_movie(self, movie_name: str) -> Optional[Movie]:
        try:
            themoviedb_input: dict = self.themoviedb_input_api.get_themoviedb_input_movie(
                movie_name=movie_name
            )
            output: Movie = Movie(
                themoviedb_input=themoviedb_input
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def create_movies(self, movie_name_list: List[str]) -> List[Movie]:
        movie_optional_list = list(map(
            lambda movie_name: self.create_movie(
                movie_name=movie_name
            ),
            movie_name_list
        ))
        output = [movie for movie in movie_optional_list if movie is not None]
        return output

    def create_movie_id(self, movie_id: int) -> Optional[Movie]:
        try:
            themoviedb_input: dict = self.themoviedb_input_api.get_themoviedb_movie_details(
                movie_id=movie_id
            )
            output: Movie = Movie(
                themoviedb_input=themoviedb_input
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def create_movies_id(self, movie_id_list: List[int]) -> List[Movie]:
        movie_optional_list = list(map(
            lambda movie_id: self.create_movie_id(
                movie_id=movie_id
            ),
            movie_id_list
        ))
        output = [movie for movie in movie_optional_list if movie is not None]
        return output

# <editor-fold desc="Libaries">
from typing import *


# </editor-fold>


class Movie:

    # <editor-fold desc="Description">
    def __init__(self, themoviedb_input: dict, omdb_input: dict):
        self.title: str = str(themoviedb_input["title"])

        self.themoviedb_status: str = str(themoviedb_input["status"])
        self.themoviedb_runtime: int = str(themoviedb_input["runtime"])
        self.themoviedb_budget: str = str(themoviedb_input["budget"])
        self.themoviedb_revenue: str = str(themoviedb_input["revenue"])
        self.themoviedb_release_date: str = str(themoviedb_input["release_date"])
        try:
            if omdb_input["Error"] is not None:
                self.omdb_awards: str = str("-")
                self.omdb_writer: str = str("-")
                self.omdb_actors: str = str("-")

        except Exception:
            self.omdb_awards: str = str(omdb_input["Awards"])
            self.omdb_writer: str = str(omdb_input["Writer"])
            self.omdb_actors: str = str(omdb_input["Actors"])

        self.themoviedb_url = str("https://www.themoviedb.org/movie/") + str(themoviedb_input["id"])
        self.themoviedb_backdrop_path: str = str("https://image.tmdb.org/t/p/w500") + str(
            themoviedb_input["backdrop_path"])
        try:
            if omdb_input["Error"] is not None:
                self.omdb_url: str = str("")

        except Exception:
            self.omdb_url = str("https://www.imdb.com/title/") + str(omdb_input["imdbID"])

        self.themoviedb_popularity: str = str(themoviedb_input["popularity"])
        self.themoviedb_vote_average: str = str(themoviedb_input["vote_average"])
        self.themoviedb_genres: List[str] = list(
            map(
                lambda genre: str(genre["name"]),
                themoviedb_input["genres"]
            )
        )
        try:
            if omdb_input["Error"] is not None:
                self.omdb_imdb_rating: str = str("-")
                self.omdb_imdb_votes: str = str("-")
                self.omdb_metascore: str = str("-")

        except Exception:
            self.omdb_imdb_rating: str = str(omdb_input["imdbRating"])
            self.omdb_imdb_votes: str = str(omdb_input["imdbVotes"])
            self.omdb_metascore: str = str(omdb_input["Metascore"])

    def json(self):
        return {
            "title": self.title,

            "themoviedb_status": self.themoviedb_status,
            "themoviedb_runtime": self.themoviedb_runtime,
            "themoviedb_budget": self.themoviedb_budget,
            "themoviedb_revenue": self.themoviedb_revenue,
            "themoviedb_release_date": self.themoviedb_release_date,
            "omdb_awards": self.omdb_awards,
            "omdb_writer": self.omdb_writer,
            "omdb_actors": self.omdb_actors,

            "themoviedb_url": self.themoviedb_url,
            "themoviedb_backdrop_path": self.themoviedb_backdrop_path,
            "omdb_url": self.omdb_url,

            "themoviedb_popularity": self.themoviedb_popularity,
            "themoviedb_vote_average": self.themoviedb_vote_average,
            "themoviedb_genres": self.themoviedb_genres,
            "omdb_imdb_rating": self.omdb_imdb_rating,
            "omdb_imdb_votes": self.omdb_imdb_votes,
            "omdb_metascore": self.omdb_metascore

        }
    # </editor-fold>

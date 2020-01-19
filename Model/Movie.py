# <editor-fold desc="Libaries">
from typing import *


# </editor-fold>


class Movie:

    # <editor-fold desc="Description">
    def __init__(self, themoviedb_input: dict):
        self.title: str = themoviedb_input["title"]

        self.themoviedb_status: str = str(themoviedb_input["status"])
        self.themoviedb_runtime: int = str(themoviedb_input["runtime"])
        self.themoviedb_budget: str = str(themoviedb_input["budget"])
        self.themoviedb_revenue: str = str(themoviedb_input["revenue"])
        self.themoviedb_release_date: str = str(themoviedb_input["release_date"])
        self.themoviedb_backdrop_path: str = str("https://image.tmdb.org/t/p/w500") + str(
            themoviedb_input["backdrop_path"])

        self.themoviedb_url = str("https://www.themoviedb.org/movie/") + str(themoviedb_input["id"])

        self.themoviedb_popularity: str = str(themoviedb_input["popularity"])
        self.themoviedb_vote_average: str = str(themoviedb_input["vote_average"])
        self.themoviedb_genres: List[str] = list(
            map(
                lambda genre: str(genre["name"]),
                themoviedb_input["genres"]
            )
        )

    def json(self):
        return {
            "title": self.title,

            "themoviedb_status": self.themoviedb_status,
            "themoviedb_runtime": self.themoviedb_runtime,
            "themoviedb_budget": self.themoviedb_budget,
            "themoviedb_revenue": self.themoviedb_revenue,
            "themoviedb_release_date": self.themoviedb_release_date,

            "themoviedb_url": self.themoviedb_url,
            "themoviedb_backdrop_path": self.themoviedb_backdrop_path,

            "themoviedb_popularity": self.themoviedb_popularity,
            "themoviedb_vote_average": self.themoviedb_vote_average,
            "themoviedb_genres": self.themoviedb_genres

        }
    # </editor-fold>

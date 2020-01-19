from typing import *
from APIs.MongoDBAPI import MongoDBAPI


class TheMovieDBChartsEPController:
    def __init__(self):
        self.mongodb_api = MongoDBAPI()
        self.chart_list = []

    def load_chart_list(self):
        self.chart_list = list(self.mongodb_api.query_movie_db(
            selection={},
            projection={
                "title": 1,

                "themoviedb_status": 1,
                "themoviedb_runtime": 1,
                "themoviedb_budget": 1,
                "themoviedb_revenue": 1,
                "themoviedb_release_date": 1,

                "themoviedb_url": 1,
                "themoviedb_backdrop_path": 1,

                "themoviedb_popularity": 1,
                "themoviedb_vote_average": 1,
                "themoviedb_genres": 1
            }
        ))
        for chart in self.chart_list:
            chart.pop("_id", None)

    def json(self) -> List[dict]:
        self.load_chart_list()
        return self.chart_list

from typing import *
from APIs.MongoDBAPI import MongoDBAPI


class MovieRecEPController:
    def __init__(self, fid):
        self.fid = fid
        self.mongodb_api = MongoDBAPI()
        self.chart_list = []
        self.genre_list = []
        self.rec_list = []

    def load_chart_list(self):
        self.chart_list = list(self.mongodb_api.query_lastfm_db(
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

    def load_genre_list(self):
        query_element = list(self.mongodb_api.query_movie_db(
            selection={"id": self.fid},
            projection={"themoviedb_genres": 1}
        ))
        genre_list_of_lists = list(map(lambda genre_list: genre_list["themoviedb_genres"], query_element))
        genre_list_not_unique = [genre for genre_list in genre_list_of_lists for genre in genre_list]
        self.genre_list = list(set(genre_list_not_unique))

    def check_list_contains(self, user_tag_list, chart_tag_list):
        for chart_tag in chart_tag_list:
            for user_tag in user_tag_list:
                if chart_tag == user_tag:
                    return True
        return False

    def create_rec_list(self):
        pass
        self.rec_list = list(filter(
            lambda chart: self.check_list_contains(self.genre_list, chart["themoviedb_genres"]),
            self.chart_list
        ))

    def json(self) -> List[dict]:
        self.load_chart_list()
        self.load_genre_list()
        self.create_rec_list()
        return self.rec_list

from flask import render_template
import logging
from APIs.MongoDBAPI import MongoDBAPI


class MoviePageController:

    def __init__(self, fid):
        self.fid = fid
        self.mongodb_api = MongoDBAPI()
        self.chart_list = []
        self.genre_list = []
        self.rec_list = []

    def load_chart_list(self):
        self.chart_list = list(self.mongodb_api.query_themoviedb_db(
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

    def get_first_element(self, element_list):
        try:
            return [element_list[0]]
        except Exception:
            return []

    def load_genre_list(self):
        query_element = list(self.mongodb_api.query_movie_db(
            selection={"id": self.fid},
            projection={"themoviedb_genres": 1}
        ))
        genre_list_of_lists = list(map(
            lambda genre_list: self.get_first_element(genre_list["themoviedb_genres"]),
            query_element
        ))
        genre_list_not_unique = [genre for genre_list in genre_list_of_lists for genre in genre_list]
        self.genre_list = list(set(genre_list_not_unique))

    def check_list_contains(self, user_tag_list, chart_tag_list):
        try:
            first_element = [chart_tag_list[0]]
            for chart_tag in first_element:
                for user_tag in user_tag_list:
                    if chart_tag == user_tag:
                        return True
            return False
        except Exception:
            return False

    def create_rec_list(self):
        self.rec_list = list(filter(
            lambda chart: self.check_list_contains(self.genre_list, chart["themoviedb_genres"]),
            self.chart_list
        ))

    def render(self):
        try:
            self.load_chart_list()
            self.load_genre_list()
            self.create_rec_list()

            webpage = render_template(
                "MoviePageView.html",
                fid=self.fid,
                chart_list=self.chart_list,
                genre_list=self.genre_list,
                rec_list=self.rec_list
            )
            return webpage
        except Exception as e:
            logging.exception(e)
            webpage = render_template(
                "ErrorPageView.html",
                function="MoviePageController.render()",
                error_type=str(type(e)),
                error=str(e)
            )
            return webpage

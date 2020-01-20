from flask import render_template
import logging

from APIs.MongoDBAPI import MongoDBAPI


class MusicPageController:

    def __init__(self, fid):
        self.fid = fid
        self.mongodb_api = MongoDBAPI()
        self.chart_list = []
        self.tag_list = []
        self.rec_list = []

    def load_chart_list(self):
        self.chart_list = list(self.mongodb_api.query_lastfm_db(
            selection={},
            projection={
                "name": 1,
                "artist": 1,

                "lastfm_duration_ms": 1,
                "spotify_duration_ms": 1,
                "spotify_explicit": 1,
                "spotify_acousticness": 1,
                "spotify_danceability": 1,
                "spotify_energy": 1,
                "spotify_instrumentalness": 1,
                "spotify_liveness": 1,
                "spotify_loudness": 1,
                "spotify_speechiness": 1,
                "spotify_valence": 1,
                "spotify_tempo": 1,

                "lastfm_url": 1,
                "spotify_url": 1,
                "spotify_preview_url": 1,
                "spotify_uri": 1,

                "lastfm_listeners": 1,
                "lastfm_playcount": 1,
                "lastfm_tags": 1,
                "spotify_popularity": 1
            }
        ))
        for chart in self.chart_list:
            chart.pop("_id", None)

    def get_first_element(self, element_list):
        try:
            return [element_list[0]]
        except Exception:
            return []

    def load_tag_list(self):
        query_element = list(self.mongodb_api.query_artist_db(
            selection={"id": self.fid},
            projection={"lastfm_tags": 1}
        ))
        tag_list_of_lists = list(map(
            lambda tag_list: self.get_first_element(tag_list["lastfm_tags"]),
            query_element
        ))
        tag_list_not_unique = [tag for tag_list in tag_list_of_lists for tag in tag_list]
        self.tag_list = list(set(tag_list_not_unique))

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
        pass
        self.rec_list = list(filter(
            lambda chart: self.check_list_contains(self.tag_list, chart["lastfm_tags"]),
            self.chart_list
        ))

    def render(self):
        try:
            self.load_chart_list()
            self.load_tag_list()
            self.create_rec_list()
            
            webpage = render_template(
                "MusicPageView.html",
                fid=self.fid,
                chart_list=self.chart_list,
                tag_list=self.tag_list,
                rec_list=self.rec_list
            )
            return webpage
        except Exception as e:
            logging.exception(e)
            webpage = render_template(
                "ErrorPageView.html",
                function="MusicPageController.render()",
                error_type=str(type(e)),
                error=str(e)
            )
            return webpage

from typing import *
from flask import render_template
import logging

from APIs.MongoDBAPI import MongoDBAPI
from Controller.FactoryController.ArtistFactoryController import ArtistFactoryController


class StatusPageController:

    # <editor-fold desc="Constructor">
    def __init__(self, fid):
        self.fid: str = fid
        self.mongodb_api: MongoDBAPI = MongoDBAPI()
        self.artist_factory: ArtistFactoryController = ArtistFactoryController()
        self.user_data: dict = None
        self.name: str = None
        self.email: str = None
        self.picture: str = None
        self.artist_name_list: List[str] = None
        self.artist_list: List[dict] = None
        self.movie_name_list = None
        self.movie_list = None

    # </editor-fold>

    # <editor-fold desc="Handle User Data">
    def load_user_data(self):
        query_element = list(self.mongodb_api.query_user_db({
            "id": self.fid
        }, None))
        self.user_data = query_element[0]

    # </editor-fold>

    # <editor-fold desc="Handle Profile Data">
    def generate_profile_data(self):
        self.name = self.user_data["name"]
        self.email = self.user_data["email"]
        self.picture = "https://graph.facebook.com/" + self.fid + "/picture?type=square"

    # </editor-fold>

    # <editor-fold desc="Handle Artist List">
    def store_artist_list(self):
        self.artist_name_list = list(map(
            lambda entry: entry["name"],
            self.user_data["music"]["data"]
        ))
        self.artist_list = self.artist_factory.create_artists(self.artist_name_list)

        for artist in self.artist_list:
            artist_list_json: dict = artist.json()
            artist_list_json["id"] = self.user_data["id"]
            if len(list(self.mongodb_api.query_artist_db(
                    {"id": self.fid, "name": artist_list_json["name"]},
                    None
            ))) == 0:
                self.mongodb_api.update_artist_db(
                    selection=None,
                    update=artist_list_json
                )
            else:
                self.mongodb_api.update_artist_db(
                    selection={"id": self.fid, "name": artist_list_json["name"]},
                    update=artist_list_json
                )
        self.user_data["artistProcessingFinished"] = True
        self.mongodb_api.update_user_db(
            selection={"id": self.user_data["id"]},
            update=self.user_data
        )

    def load_artist_list(self):
        self.artist_list = list(self.mongodb_api.query_artist_db({
            "id": self.fid
        }, None))

    def delete_artist_list(self):
        self.mongodb_api.delete_artist_db({
            "id": self.fid
        })

    # </editor-fold>

    # <editor-fold desc="Handle Movie List">

    def store_movie_list(self):
        self.movie_list = list(map(
            lambda entry: entry["name"],
            self.user_data["movies"]["data"]
        ))

    def load_movie_list(self):
        self.movie_list = list(map(
            lambda entry: entry["name"],
            self.user_data["movies"]["data"]
        ))

    def delete_movie_list(self):
        self.mongodb_api.delete_movie_db({
            "id": self.fid
        })

    # </editor-fold>

    # <editor-fold desc="Render">
    def render(self):
        try:
            self.load_user_data()
            self.generate_profile_data()
            if not self.user_data["artistProcessingFinished"]:
                self.store_artist_list()
            self.load_artist_list()
            if not self.user_data["movieProcessingFinished"]:
                self.store_movie_list()
            self.load_movie_list()

            self.artist_list.sort(key=lambda artist: artist["name"])
            webpage = render_template(
                "StatusPageView.html",
                userName=self.name,
                userEmail=self.email,
                userPicture=self.picture,
                artistList=self.artist_list,
                movieList=self.movie_list
            )
            return webpage
        except Exception as e:
            logging.exception(e)
            webpage = render_template(
                "ErrorPageView.html",
                function="StatusPageController.render()",
                error_type=str(type(e)),
                error=str(e)
            )
            return webpage
    # </editor-fold>

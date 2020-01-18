from typing import *
from flask import render_template
import logging

from APIs.MongoDBAPI import MongoDBAPI
from Controller.FactoryController.ArtistFactoryController import ArtistFactoryController
from Controller.FactoryController.MovieFactoryController import MovieFactoryController


class StatusPageController:

    # <editor-fold desc="Constructor">
    def __init__(self, fid):
        self.fid: str = fid
        self.mongodb_api: MongoDBAPI = MongoDBAPI()
        self.artist_factory_controller: ArtistFactoryController = ArtistFactoryController()
        self.movie_factory_controller: MovieFactoryController = MovieFactoryController()
        self.user_data: dict = None
        self.name: str = None
        self.email: str = None
        self.picture: str = None
        self.artist_name_list: List[str] = None
        self.artist_list: List[dict] = None
        self.movie_name_list: List[str] = None
        self.movie_list: List[dict] = None

    # </editor-fold>

    # <editor-fold desc="Handle User Data">
    def load_user_data(self):
        query_element = list(self.mongodb_api.query_user_db(
            selection={"id": self.fid},
            projection=None))
        self.user_data = query_element[0]

    # </editor-fold>

    # <editor-fold desc="Handle Profile Data">
    def generate_profile_data(self):
        self.name = self.user_data["name"]
        self.email = self.user_data["email"]
        self.picture = "https://graph.facebook.com/" + self.fid + "/picture?type=square"

    # </editor-fold>

    # <editor-fold desc="Handle Lists">
    def store_lists(self):
        self.artist_name_list = list(map(
            lambda entry: entry["name"],
            self.user_data["music"]["data"]
        ))
        self.movie_name_list = list(map(
            lambda entry: entry["name"],
            self.user_data["movies"]["data"]
        ))

        self.artist_list = self.artist_factory_controller.create_artists(artist_name_list=self.artist_name_list)
        self.movie_list = self.movie_factory_controller.create_movies(movie_name_list=self.movie_name_list)

        for artist in self.artist_list:
            artist_json: dict = artist.json()
            artist_json["id"] = self.user_data["id"]
            self.mongodb_api.update_artist_db(
                selection=None,
                update=artist_json
            )
        for movie in self.movie_list:
            movie_json: dict = movie.json()
            movie_json["id"] = self.user_data["id"]
            self.mongodb_api.update_movie_db(
                selection=None,
                update=movie_json
            )
        self.user_data["processingFinished"] = True
        self.mongodb_api.update_user_db(
            selection={"id": self.user_data["id"]},
            update=self.user_data
        )

    def load_lists(self):
        self.artist_list = list(self.mongodb_api.query_artist_db(
            selection={"id": self.fid},
            projection=None
        ))
        self.movie_list = list(self.mongodb_api.query_movie_db(
            selection={"id": self.fid},
            projection=None
        ))

    def delete_lists(self):
        self.mongodb_api.delete_artist_db(
            delete={"id": self.fid}
        )
        self.mongodb_api.delete_movie_db(
            delete={"id": self.fid}
        )

    # </editor-fold>

    # <editor-fold desc="Render">
    def render(self):
        try:
            self.load_user_data()
            self.generate_profile_data()
            if not self.user_data["processingFinished"]:
                self.delete_lists()
                self.store_lists()
            else:
                self.load_lists()

            print("Artist type: " + str(type(artist_list)))
            self.artist_list.sort(key=lambda artist: artist["name"])
            self.movie_list.sort(key=lambda movie: movie["title"])

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

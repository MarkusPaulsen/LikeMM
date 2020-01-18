from typing import *
from flask import render_template, redirect

from APIs.FacebookAPI import FacebookAPI
from APIs.MongoDBAPI import MongoDBAPI


class UserEntryController:

    def __init__(self, code):
        self.facebook_api: FacebookAPI = FacebookAPI()
        self.mongo_db_api: MongoDBAPI = MongoDBAPI()
        self.code: str = code
        self.access_token = None
        self.user_data = None

    def generate_access_token(self):
        generate_access_token_success, access_token = self.facebook_api.generate_access_token(
            code=self.code
        )
        if generate_access_token_success:
            self.access_token = access_token

    def generate_user_data(self):
        generate_user_data_success, user_data = self.facebook_api.generate_user_data(
            fields="id, name, email, music, movies",
            access_token=self.access_token
        )
        if generate_user_data_success:
            self.access_token = user_data

    def store_user_data_access_token(self):
        self.mongo_db_api.insert_user_db(entry_to_insert={
            "id": self.user_data["id"],
            "name": self.user_data["name"],
            "email": self.user_data["email"],
            "music": self.user_data["music"],
            "movies": self.user_data["movies"],
            "facebookToken": self.access_token
        })

    def delete_artists(self):
        self.mongo_db_api.delete_artist_db({
            "id": self.user_data["id"]
        })


    def render(self):
        try:
            # <editor-fold desc="1st Facebook API call">
            self.generate_access_token()
            # </editor-fold>

            if self.access_token is not None:

                # <editor-fold desc="2nd Facebook API call">
                self.generate_user_data()
                # </editor-fold>

                if self.user_data is not None:

                    # <editor-fold desc="MongoDB store">
                    self.store_user_data_access_token()
                    # </editor-fold>

                    # <editor-fold desc="MongoDB delete">

                    # </editor-fold>

                    webpage = redirect(
                        location="/Status/" + str(self.user_data["id"]),
                        code=302
                    )
                    return webpage
                else:
                    webpage = render_template(
                        "ErrorPageView.html",
                        function="facebook_login_reply_page()",
                        error_type="",
                        error="User data of Facebook cannot be generated."
                    )
                    return webpage
            else:
                webpage = render_template(
                    "ErrorPageView.html",
                    function="facebook_login_reply_page()",
                    error_type="",
                    error="Access token for Facebook cannot be generated."
                )
                return webpage

        except Exception as e:
            logging.exception(e)
            webpage = render_template(
                "ErrorPageView.html",
                function="facebook_login_reply_page()",
                error_type=str(type(e)),
                error=str(e)
            )
            return webpage
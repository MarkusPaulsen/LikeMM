from flask import render_template, redirect
import logging

from APIs.MongoDBAPI import MongoDBAPI


class ResetProcessedEntryController:

    def __init__(self, fid):
        self.fid = fid
        self.mongodb_api: MongoDBAPI = MongoDBAPI()
        self.user_data = {}

    # <editor-fold desc="Handle User Data">
    def delete_user_data(self):
        self.mongodb_api.delete_artist_db(
            delete={"id": self.fid}
        )
        self.mongodb_api.delete_movie_db(
            delete={"id": self.fid}
        )
        self.mongodb_api.delete_user_db(
            delete={"id": self.fid}
        )

    # </editor-fold>

    def render(self):
        try:
            self.delete_user_data()
            webpage = redirect(
                location="/",
                code=302
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

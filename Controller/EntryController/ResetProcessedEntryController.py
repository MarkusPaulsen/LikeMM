from flask import render_template, redirect
import logging

from APIs.MongoDBAPI import MongoDBAPI


class ResetProcessedEntryController:

    def __init__(self, fid):
        self.fid = fid
        self.mongodb_api: MongoDBAPI = MongoDBAPI()
        self.user_data = {}

    # <editor-fold desc="Handle User Data">
    def load_user_data(self):
        query_element = list(self.mongodb_api.query_user_db(
            selection={"id": self.fid},
            projection=None))
        self.user_data = query_element[0]

    def reset_processed(self):
        self.user_data["processingFinished"] = False
        self.mongodb_api.update_user_db(
            selection={"id": self.fid},
            update=self.user_data
        )

    # </editor-fold>

    def render(self):
        try:
            self.reset_processed()
            webpage = redirect(
                location="/Status/" + str(self.fid),
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

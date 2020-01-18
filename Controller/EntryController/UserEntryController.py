from flask import render_template, redirect
import logging

from APIs.FacebookAPI import FacebookAPI
from APIs.MongoDBAPI import MongoDBAPI


class UserEntryController:

    def __init__(self, code):
        self.facebook_api: FacebookAPI = FacebookAPI()
        self.mongodb_api: MongoDBAPI = MongoDBAPI()
        self.code: str = code
        self.user_data: dict = {
            "access_token": None,
            "id": None
        }

    def generate_access_token(self):
        generate_access_token_success, access_token = self.facebook_api.generate_access_token(
            code=self.code
        )
        if generate_access_token_success:
            self.user_data["access_token"] = access_token

    def generate_user_data(self):
        generate_user_data_success, facebook_data = self.facebook_api.generate_user_data(
            fields="id, name, email, music, movies",
            access_token=self.user_data["access_token"]
        )
        if generate_user_data_success:
            self.user_data["id"] = facebook_data["id"]
            self.user_data["name"] = facebook_data["name"]
            self.user_data["email"] = facebook_data["email"]
            self.user_data["music"] = facebook_data["music"]
            self.user_data["movies"] = facebook_data["movies"]

    def check_user_not_registered(self) -> bool:
        user_list: list = list(self.mongodb_api.query_user_db(
            selection={"id": self.user_data["id"]},
            projection={"id": self.user_data["id"]}
        ))
        is_user_registered: bool = len(user_list) == 0
        return is_user_registered

    def register_user(self):
        self.user_data["processingFinished"] = False
        self.mongodb_api.update_user_db(
            selection=None,
            update=self.user_data
        )

    def render(self):
        try:
            # <editor-fold desc="1st Facebook API call">
            self.generate_access_token()
            # </editor-fold>

            if self.user_data["access_token"] is not None:

                # <editor-fold desc="2nd Facebook API call">
                self.generate_user_data()
                # </editor-fold>

                if self.user_data["id"] is not None:

                    if self.check_user_not_registered():

                        # <editor-fold desc="MongoDB store">
                        self.register_user()
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

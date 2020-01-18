# <editor-fold desc="Libaries">
from typing import *
import os
import requests
import json
# </editor-fold>


# noinspection PyMethodMayBeStatic
class FacebookAPI:
    def __init__(self):
        self.facebook_app_id = os.environ["facebook_app_id"]
        self.facebook_redirect_url = os.environ["facebook_redirect_url"]
        self.facebook_client_secret = os.environ["facebook_client_secret"]

    # <editor-fold desc="Login page">
    def get_facebook_login_page(self, state: int) -> str:
        return ("https://www.facebook.com/v5.0/dialog/oauth?"
                + "client_id=" + self.facebook_app_id
                + "&redirect_uri=" + self.facebook_redirect_url
                + "&state=" + str(state)
                )
    # </editor-fold>

    # <editor-fold desc="Access token">
    def generate_access_token(self, code: str) -> Tuple[bool, str]:
        reply: requests.models.Response = requests.get(
            url=("https://graph.facebook.com/v5.0/oauth/access_token?"
                 + "client_id=" + self.facebook_app_id
                 + "&redirect_uri=" + self.facebook_redirect_url
                 + "&client_secret=" + self.facebook_client_secret
                 + "&code=" + code)
        )
        if reply.status_code == 200:
            response_json: str = reply.text
            response: dict = json.loads(s=response_json)
            response_token: str = response["access_token"]
            return True, response_token
        else:
            return False, ""
    # </editor-fold>

    # <editor-fold desc="User data">
    def generate_user_data(self, fields: str, access_token: str) -> Tuple[bool, dict]:
        reply: requests.models.Response = requests.get(
            url=("https://graph.facebook.com/me?"
                 + "fields=" + fields
                 + "&access_token=" + access_token)
        )
        if reply.status_code == 200:
            response_json: str = reply.text
            response: dict = json.loads(s=response_json)
            return True, response
        else:
            return False, {}
    # </editor-fold>

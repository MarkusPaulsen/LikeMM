# <editor-fold desc="Libaries">
import os
import json
import requests
import rx
from rx import operators as ops
import operator


# </editor-fold>


# noinspection PyMethodMayBeStatic
class FacebookAPI:

    # <editor-fold desc="Login page">
    def get_facebook_login_page(self, state: int) -> str:
        output = rx \
            .just(
            "https://www.facebook.com/v5.0/dialog/oauth?"
            + "client_id=" + os.environ["facebook_app_id"]
            + "&redirect_uri=" + os.environ["facebook_redirect_url"]
            + "&state=" + str(state)
        ) \
            .run()
        return output

    # </editor-fold>

    # <editor-fold desc="Access token">
    def generate_access_token(self, code: str) -> (bool, str):

        def transform_reply(reply):
            if reply.status_code == 200:
                response_json: str = reply.text
                response: dict = json.loads(s=response_json)
                response_token: str = response["access_token"]
                return True, response_token
            else:
                return False, ""

        output = rx \
            .just("https://graph.facebook.com/v5.0/oauth/access_token?"
                  + "client_id=" + os.environ["facebook_app_id"]
                  + "&redirect_uri=" + os.environ["facebook_redirect_url"]
                  + "&client_secret=" + os.environ["facebook_client_secret"]
                  + "&code=" + code) \
            .pipe(ops.map(lambda address:
                          requests.get(url=address)
                          )) \
            .pipe(ops.map(lambda reply:
                          transform_reply(reply)
                          ))\
            .run()
        return output

    # </editor-fold>

    # <editor-fold desc="User data">
    def generate_user_data(self, fields: str, access_token: str) -> (bool, dict):

        def transform_reply(reply):
            if reply.status_code == 200:
                response_json: str = reply.text
                response: dict = json.loads(s=response_json)
                return True, response
            else:
                return False, []

        output = rx \
            .just("https://graph.facebook.com/me?"
                 + "fields=" + fields
                 + "&access_token=" + access_token) \
            .pipe(ops.map(lambda address:
                          requests.get(url=address)
                          )) \
            .pipe(ops.map(lambda reply:
                          transform_reply(reply)
                          )) \
            .run()
        return output
    # </editor-fold>

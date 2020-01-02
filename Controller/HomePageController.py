from flask import render_template
import random
import logging

from APIs.FacebookAPI import FacebookAPI


class HomePageController:

    def __init__(self):
        self.facebook_api: FacebookAPI = FacebookAPI()

    def get_facebook_login_page_link(self) -> str:
        random_number: int = random.randint(0, 1000000)
        return self.facebook_api.get_facebook_login_page(state=random_number)

    def render(self):
        try:
            webpage = render_template(
                "HomePageView.html",
                facebook_login_page_link=self.get_facebook_login_page_link()
            )
            return webpage
        except Exception as e:
            logging.exception(e)
            webpage = render_template(
                "ErrorPageView.html",
                function="HomePageController.render()",
                error_type=str(type(e)),
                error=str(e)
            )
            return webpage

from flask import render_template
import logging


class MusicPageController:

    def __init__(self, fid):
        self.fid = fid

    def render(self):
        try:
            webpage = render_template("MusicPageView.html")
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

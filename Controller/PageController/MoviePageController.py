from flask import render_template
import logging


class MoviePageController:

    def __init__(self, fid):
        self.fid = fid

    def render(self):
        try:
            webpage = render_template(
                "MoviePageView.html",
                fid=self.fid,
            )
            return webpage
        except Exception as e:
            logging.exception(e)
            webpage = render_template(
                "ErrorPageView.html",
                function="MoviePageController.render()",
                error_type=str(type(e)),
                error=str(e)
            )
            return webpage

from flask import render_template


class MoviePageController:

    def __init__(self, fid):
        self.fid = fid

    def render(self):
        try:
            webpage = render_template("MoviePageView.html")
            return webpage
        except Exception as e:
            webpage = render_template(
                "ErrorPageView.html",
                function="home_page()",
                error_type=str(type(e)),
                error=str(e)
            )
            return webpage
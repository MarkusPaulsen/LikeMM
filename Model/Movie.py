# <editor-fold desc="Libaries">
from typing import *
# </editor-fold>


class Movie:

    # <editor-fold desc="Description">
    def __init__(self, themoviedb_input: dict):
        self.original_title: str = themoviedb_input["original_title"]

    def json(self):
        return {
            "original_title": self.original_title,
        }
    # </editor-fold>

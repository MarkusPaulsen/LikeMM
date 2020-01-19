# <editor-fold desc="Libaries">
from typing import *
import billboard
# </editor-fold>


# noinspection PyMethodMayBeStatic
class BillboardInputAPI:

    def get_billboard_charts(self):
        return billboard.charts()

    def get_billboard_input_track(self, track_name: str, track_artist: str) -> Optional[dict]:
        try:
            hot100_entries = billboard.ChartData('hot-100').entries
            billboard_list: list = list(filter(
                lambda chart: (chart.title.lower() == track_name.lower() and chart.artist.lower() == track_artist.lower()),
                hot100_entries
            ))
            if len(billboard_list) == 0:
                output: dict = {
                    "artist": "-",
                    "image": "-",
                    "isNew": "-",
                    "lastPos": "-",
                    "peakPos": "-",
                    "rank": "-",
                    "title": "-",
                    "weeks": "-"
                }
            else:
                output: dict = {
                    "artist": billboard_list[0].artist,
                    "image": billboard_list[0].image,
                    "isNew": billboard_list[0].isNew,
                    "lastPos": billboard_list[0].lastPos,
                    "peakPos": billboard_list[0].peakPos,
                    "rank": billboard_list[0].rank,
                    "title": billboard_list[0].title,
                    "weeks": billboard_list[0].weeks
                }
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def get_lastfm_input_artist(self, artist_name: str) -> Optional[dict]:
        try:
            artist100_entries = billboard.ChartData('artist-100').entries
            billboard_list: list = list(filter(
                lambda chart: (chart.artist.lower() == artist_name.lower()),
                artist100_entries
            ))
            if len(billboard_list) == 0:
                output: dict = {
                    "artist": "-",
                    "image": "-",
                    "isNew": "-",
                    "lastPos": "-",
                    "peakPos": "-",
                    "rank": "-",
                    "title": "-",
                    "weeks": "-"
                }
            else:
                output: dict = {
                    "artist": billboard_list[0].artist,
                    "image": billboard_list[0].image,
                    "isNew": billboard_list[0].isNew,
                    "lastPos": billboard_list[0].lastPos,
                    "peakPos": billboard_list[0].peakPos,
                    "rank": billboard_list[0].rank,
                    "title": billboard_list[0].title,
                    "weeks": billboard_list[0].weeks
                }
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

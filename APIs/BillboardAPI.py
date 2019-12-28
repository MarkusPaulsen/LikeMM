from typing import *
import billboard

from Model.Track import Track


# noinspection PyMethodMayBeStatic
class BillboardAPI:

    def billboard_chart_get_top_tracks(self) -> Optional[List[Track]]:
        try:
            output_with_none: List[Optional[Track]] = list(
                map(
                    lambda entry: Track(input_data={
                        "name": entry.title,
                        "url": entry.rank,
                        "listeners": entry.lastPos,
                        "playcount": entry.weeks,
                        "artist": {
                            "name": entry.artist
                        },
                        "toptags": {
                            "tag": []
                        }
                    }),
                    billboard.ChartData('hot-100').entries)
            )
            output: List[Track] = list(filter(
                None,
                output_with_none
            ))
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None
x1=billboard.ChartData('hot-100').entries
z=0
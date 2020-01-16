from flask import Flask, request, jsonify
import pprint

from Controller.PageController.HomePageController import HomePageController
from Controller.PageController.StatusPageController import StatusPageController
from Controller.PageController.MusicPageController import MusicPageController
from Controller.PageController.MoviePageController import MoviePageController
from Controller.PageController.ErrorPageController import ErrorPageController
from Controller.EntryController.UserEntryController import UserEntryController
from Controller.EndpointController.LastFMTopEPController import LastFMTopEPController
from Controller.EndpointController.UserTagsEPController import UserTagsEPController

from APIs.LastFmAPI import LastFmAPI
from APIs.MongoDBAPI import MongoDBAPI
from APIs.BillboardInputAPI import BillboardInputAPI

lastfm_api: LastFmAPI = LastFmAPI()
mongodb_api: MongoDBAPI = MongoDBAPI()

mongodb_api.delete_last_fm_chart_db({})
for track in lastfm_api.get_lastfm_charts(10):
    mongodb_api.update_last_fm_chart_db(selection=None, update=track.json())

billboard_input_api: BillboardInputAPI = BillboardInputAPI()
x = billboard_input_api.get_billboard_input_track("a", "s")
pprint.pprint(x)

app = Flask(__name__)


@app.route("/")
def home_page():
    home_page_controller: HomePageController = HomePageController()
    return home_page_controller.render()


@app.route("/facebookLoginReply")
def facebook_login_reply_page():
    user_entry_controller: UserEntryController = UserEntryController(code=request.args.get("code"))
    return user_entry_controller.render()


@app.route("/Status/<fid>")
def status_page(fid):
    if fid == "alt=":
        return None
    else:
        status_page_controller: StatusPageController = StatusPageController(fid)
        return status_page_controller.render()


@app.route("/Music/<fid>")
def music_page(fid):
    music_page_controller: MusicPageController = MusicPageController(fid)
    return music_page_controller.render()


@app.route("/Movie/<fid>")
def movie_page(fid):
    movie_page_controller: MoviePageController = MoviePageController(fid)
    return movie_page_controller.render()


@app.route("/Error/<fid>")
def error_page(fid):
    error_page_controller: ErrorPageController = ErrorPageController(fid)
    return error_page_controller.render()


@app.route('/json/lastFMTop/<nr>', methods=['GET'])
def last_fm_top_ep(nr):
    last_fm_top_ep_controller: LastFMTopEPController = LastFMTopEPController()
    return jsonify(last_fm_top_ep_controller.json(nr))


@app.route('/json/userTags/<fid>', methods=['GET'])
def user_tags(fid):
    user_tags_ep_controller: UserTagsEPController = UserTagsEPController(fid)
    return jsonify(user_tags_ep_controller.json())

# @app.route("/process/<idnr>/<target>")
# def process_page(idnr, target):
#     try:
#
#         if target == "artists":
#
#             # <editor-fold desc="MongoDB delete">
#             mongo_db_api.delete_artist_db({
#                 "id": idnr
#             })
#             # </editor-fold>
#
#             # <editor-fold desc="MongoDB query">
#             access_token: str = list(map(
#                 lambda credentials: credentials["token"],
#                 mongo_db_api.query_credentials_db({"name": "facebook"}, {"token": 1})
#             ))[0]
#             # </editor-fold>
#
#             # <editor-fold desc="Facebook API call">
#             generate_user_data_success, user_data = facebook_api.generate_user_data(
#                 fields="music",
#                 access_token=access_token
#             )
#             # </editor-fold>
#
#             if generate_user_data_success:
#
#                 # <editor-fold desc="1st Last.FM API call">
#                 artist_list: List[Artist] = list(map(
#                     lambda music: lasfm_api.lastfm_artist_get_info(artist=music["name"]),
#                     user_data["music"]["data"]
#                 ))
#
#                 # </editor-fold>
#
#                 # <editor-fold desc="Remove Duplicate">
#                 def remove_duplicate(track_list: List[Artist]) -> List[Artist]:
#                     track_list_nd = []
#                     for track in track_list:
#                         track_list_nd_name_list = list(map(
#                             lambda track_map: track_map.name,
#                             track_list_nd
#                         ))
#                         if track.name not in track_list_nd_name_list:
#                             track_list_nd = track_list_nd + [track]
#                     return track_list_nd
#
#                 artist_list_nd: List[Artist] = remove_duplicate(artist_list)
#
#                 # </editor-fold>
#
#                 # <editor-fold desc="MongoDB store">
#                 def store_track_list(artist_list_nd: List[Artist]):
#                     for artist in artist_list_nd:
#                         mongo_db_api.insert_artist_db({
#                             "id": idnr,
#                             "name": artist.name,
#                             "lastfm_url": artist.lastfm_url,
#                             "lastfm_listeners": artist.lastfm_listeners,
#                             "lastfm_playcount": artist.lastfm_playcount,
#                             "image": artist.image,
#                             "toptags": reduce(
#                                 lambda part1, part2: part1 + "," + part2,
#                                 map(lambda tag: tag.name, artist.toptags)
#                             )
#                         })
#
#                 store_track_list(artist_list_nd)
#                 # </editor-fold>
#
#                 webpage = redirect(location="/artists/" + idnr, code=302)
#                 return webpage
#             else:
#                 webpage = render_template("ErrorPageView.html", function="process_page(idnr)", error_type="",
#                                           error="Music of Facebook cannot be generated")
#                 return webpage
#
#         if target == "suggestions":
#
#             # <editor-fold desc="MongoDB delete">
#             mongo_db_api.delete_music_db({
#                 "id": idnr
#             })
#             # </editor-fold>
#
#             # <editor-fold desc="1st MongoDB query">
#             artist_name_list: List[str] = list(map(
#                 lambda artist: artist["name"],
#                 mongo_db_api.query_artist_db({"id": idnr}, {"name": 1})
#             ))
#
#             artist_toptags_list: List[str] = list(map(
#                 lambda artist: artist["toptags"],
#                 mongo_db_api.query_artist_db({"id": idnr}, {"toptags": 1})
#             ))
#             # </editor-fold>
#
#             # <editor-fold desc="1st List Processing">
#             artist_name_list_nd: List[str] = list(dict.fromkeys(artist_name_list))
#
#             all_artists_toptags: str = reduce(
#                 lambda old, new: old + "," + new,
#                 artist_toptags_list
#             )
#             all_artists_toptags_list: List[str] = all_artists_toptags.split(",")
#             all_artists_toptags_list_nd: List[str] = list(dict.fromkeys(all_artists_toptags_list))
#
#             # </editor-fold>
#
#             # <editor-fold desc="1st Last.FM API call">
#             artist_top_track_list_of_lists: List[List[Track]] = list(map(
#                 lambda artist: lasfm_api.lastfm_artist_get_top_tracks(artist=artist),
#                 artist_name_list_nd
#             ))
#
#             artist_similar_list_of_lists: List[List[Artist]] = list(map(
#                 lambda artist: lasfm_api.lastfm_artist_get_similar(artist=artist),
#                 artist_name_list_nd
#             ))
#
#             tag_top_track_list_of_lists: List[List[Track]] = list(map(
#                 lambda tag: lasfm_api.lastfm_tag_get_top_tracks(tag),
#                 all_artists_toptags_list_nd
#             ))
#
#             # </editor-fold>
#
#             # <editor-fold desc="2nd List Processing">
#             def merge_and_remove_none(list_of_lists_with_none: List[Optional[list]]) -> list:
#                 list_of_lists: List[Track] = list(filter(
#                     None,
#                     list_of_lists_with_none
#                 ))
#                 list_with_none: List[Optional[Track]] = reduce(
#                     list.__add__,
#                     list_of_lists
#                 )
#                 list_output: List[Track] = list(filter(
#                     None,
#                     list_with_none
#                 ))
#                 return list_output
#
#             artist_top_track_list: List[Track] = merge_and_remove_none(artist_top_track_list_of_lists)
#
#             artist_similar_list: List[Artist] = merge_and_remove_none(artist_similar_list_of_lists)
#
#             tag_top_track_list: List[Track] = merge_and_remove_none(tag_top_track_list_of_lists)
#             # </editor-fold>
#
#             # <editor-fold desc="2st Last.FM API call">
#             artist_similar_top_track_list_of_lists: List[List[Artist]] = list(map(
#                 lambda artist_similar: lasfm_api.lastfm_artist_get_top_tracks(artist=artist_similar.name),
#                 artist_similar_list
#             ))
#             # </editor-fold>
#
#             # <editor-fold desc="3nd List Processing">
#             artist_similar_top_track_list: List[Track] = merge_and_remove_none(artist_similar_top_track_list_of_lists)
#
#             # </editor-fold>
#
#             # <editor-fold desc="Remove Duplicate">
#             def remove_duplicate(track_list: List[Track]) -> List[Track]:
#                 track_list_nd = []
#                 for track in track_list:
#                     track_list_nd_name_list = list(map(
#                         lambda track_map: track_map.name,
#                         track_list_nd
#                     ))
#                     if track.name not in track_list_nd_name_list:
#                         track_list_nd = track_list_nd + [track]
#                 return track_list_nd
#
#             artist_top_track_list_nd: List[Track] = remove_duplicate(artist_top_track_list)
#
#             artist_similar_top_track_list_nd: List[Track] = remove_duplicate(artist_similar_top_track_list)
#
#             tag_top_track_list_nd: List[Track] = remove_duplicate(tag_top_track_list)
#
#             # </editor-fold>
#
#             # <editor-fold desc="MongoDB store">
#             def store_track_list(track_list_nd: List[Track]):
#                 for track in track_list_nd:
#                     mongo_db_api.insert_music_db({
#                         "id": idnr,
#                         "name": track.name,
#                         "artist": track.artist,
#                         "lastfm_url": track.lastfm_url,
#                         "lastfm_listeners": track.lastfm_listeners,
#                         "lastfm_playcount": track.lastfm_playcount
#                     })
#
#             store_track_list(artist_top_track_list_nd)
#             store_track_list(artist_similar_top_track_list_nd)
#             store_track_list(tag_top_track_list_nd)
#             # </editor-fold>
#
#             webpage = redirect(location="/suggestions/" + idnr, code=302)
#             return webpage
#
#         if target == "top10":
#
#             # <editor-fold desc="MongoDB delete">
#             mongo_db_api.delete_top10_db({
#                 "id": idnr
#             })
#             # </editor-fold>
#
#             # <editor-fold desc="1st Last.FM API call">
#             charts_top_track_list_with_none: List[Track] = lasfm_api.lastfm_chart_get_top_tracks()
#
#             # </editor-fold>
#
#             # <editor-fold desc="2nd List Processing">
#             def merge_and_remove_none(track_list: List[Optional[Track]]) -> List[Track]:
#                 track_list_output: List[Track] = list(filter(
#                     None,
#                     track_list
#                 ))
#                 return track_list_output
#
#             charts_top_track_list: List[Track] = merge_and_remove_none(charts_top_track_list_with_none)
#
#             # </editor-fold>
#
#             # <editor-fold desc="Remove Duplicate">
#             def remove_duplicate(track_list: List[Track]) -> List[Track]:
#                 track_list_nd = []
#                 for track in track_list:
#                     track_list_nd_name_list = list(map(
#                         lambda track_map: track_map.name,
#                         track_list_nd
#                     ))
#                     if track.name not in track_list_nd_name_list:
#                         track_list_nd = track_list_nd + [track]
#                 return track_list_nd
#
#             charts_top_track_list_nd: List[Track] = remove_duplicate(charts_top_track_list)
#
#             # </editor-fold>
#
#             # <editor-fold desc="MongoDB store">
#             def store_track_list(track_list_nd: List[Track]):
#                 for track in track_list_nd:
#                     mongo_db_api.insert_top10_db({
#                         "id": idnr,
#                         "name": track.name,
#                         "artist": track.artist,
#                         "lastfm_url": track.lastfm_url,
#                         "lastfm_listeners": track.lastfm_listeners,
#                         "lastfm_playcount": track.lastfm_playcount
#                     })
#
#             store_track_list(charts_top_track_list_nd)
#             # </editor-fold>
#
#             webpage = redirect(location="/top10/" + idnr, code=302)
#             return webpage
#
#         if target == "billboard":
#
#             # <editor-fold desc="MongoDB delete">
#             mongo_db_api.delete_billboard_db({
#                 "id": idnr
#             })
#             # </editor-fold>
#
#             # <editor-fold desc="1st Billboard API call">
#             billboard_top_track_list_with_none: List[Track] = billboard_api.billboard_chart_get_top_tracks()
#             # </editor-fold>
#
#             # <editor-fold desc="2nd List Processing">
#             def merge_and_remove_none(track_list: List[Optional[Track]]) -> List[Track]:
#                 track_list_output: List[Track] = list(filter(
#                     None,
#                     track_list
#                 ))
#                 return track_list_output
#
#             billboard_top_track_list: List[Track] = merge_and_remove_none(billboard_top_track_list_with_none)
#
#             # </editor-fold>
#
#             # <editor-fold desc="Remove Duplicate">
#             def remove_duplicate(track_list: List[Track]) -> List[Track]:
#                 track_list_nd = []
#                 for track in track_list:
#                     track_list_nd_name_list = list(map(
#                         lambda track_map: track_map.name,
#                         track_list_nd
#                     ))
#                     if track.name not in track_list_nd_name_list:
#                         track_list_nd = track_list_nd + [track]
#                 return track_list_nd
#
#             billboard_top_track_list_nd: List[Track] = remove_duplicate(billboard_top_track_list)
#
#             # </editor-fold>
#
#             # <editor-fold desc="MongoDB store">
#             def store_track_list(track_list_nd: List[Track]):
#                 for track in track_list_nd:
#                     mongo_db_api.insert_billboard_db({
#                         "id": idnr,
#                         "name": track.name,
#                         "artist": track.artist,
#                         "lastfm_url": track.lastfm_url,
#                         "lastfm_listeners": track.lastfm_listeners,
#                         "lastfm_playcount": track.lastfm_playcount
#                     })
#
#             store_track_list(billboard_top_track_list_nd)
#             # </editor-fold>
#
#             webpage = redirect(location="/billboard/" + idnr, code=302)
#             return webpage
#
#     except Exception as e:
#         webpage = render_template("ErrorPageView.html",
#         function="process_page(idnr, target)", error_type=str(type(e)),
#         error=str(e))
#         return webpage
#
#
# @app.route("/artists/<idnr>")
# def artists_page(idnr):
#     try:
#
#         # <editor-fold desc="MongoDB query">
#         user_name: List[str] = list(map(
#             lambda users: users["name"],
#             mongo_db_api.query_user_db({"id": idnr}, {"name": 1})
#         ))[0]
#
#         artist_list = list(mongo_db_api.query_artist_db({
#             "id": idnr
#         }, {
#             "name": 1,
#             "lastfm_url": 1,
#             "lastfm_listeners": 1,
#             "lastfm_playcount": 1,
#             "image": 1,
#             "toptags": 1
#         }))
#         # </editor-fold>
#
#         # <editor-fold desc="List processing">
#         artist_list.sort(reverse=True, key=lambda artist: int(artist["lastfm_listeners"]))
#         # </editor-fold>
#
#         webpage = render_template("artists.html", idnr=idnr, artist_list=artist_list, user_name=user_name)
#         return webpage
#     except Exception as e:
#         webpage = render_template("ErrorPageView.html", function="artists_page(idnr)", error_type=str(type(e)),
#                                   error=str(e))
#         return webpage
#
#
# @app.route("/suggestions/<idnr>")
# def suggestion_page(idnr):
#     try:
#
#         # <editor-fold desc="MongoDB query">
#         user_name: List[str] = list(map(
#             lambda users: users["name"],
#             mongo_db_api.query_user_db({"id": idnr}, {"name": 1})
#         ))[0]
#
#         suggestions: list = list(mongo_db_api.query_music_db({
#             "id": idnr
#         }, {
#             "name": 1,
#             "lastfm_url": 1,
#             "lastfm_listeners": 1,
#             "lastfm_playcount": 1,
#             "artist": 1,
#             "album": 1,
#             "album_creator": 1,
#         }).sort("lastfm_listeners", -1))
#         # </editor-fold>
#
#         # <editor-fold desc="List procesing">
#         suggestions.sort(reverse=True, key=(lambda track: int(track["lastfm_listeners"])))
#         # </editor-fold>
#
#         webpage = render_template("suggestions.html", idnr=idnr, suggestions=suggestions, user_name=user_name)
#         return webpage
#     except Exception as e:
#         webpage = render_template("ErrorPageView.html", function="suggestion_page(idnr)", error_type=str(type(e)),
#                                   error=str(e))
#         return webpage
#
#
# @app.route("/top10/<idnr>")
# def top10_page(idnr):
#     try:
#
#         # <editor-fold desc="MongoDB query">
#         user_name: List[str] = list(map(
#             lambda users: users["name"],
#             mongo_db_api.query_user_db({"id": idnr}, {"name": 1})
#         ))[0]
#
#         top10_list: list = list(mongo_db_api.query_top10_db({
#             "id": idnr
#         }, {
#             "name": 1,
#             "lastfm_url": 1,
#             "lastfm_listeners": 1,
#             "lastfm_playcount": 1,
#             "artist": 1,
#             "album": 1,
#             "album_creator": 1,
#         }).sort("lastfm_listeners", -1))
#         # </editor-fold>
#
#         # <editor-fold desc="List procesing">
#         top10_list.sort(reverse=True, key=(lambda track: int(track["lastfm_listeners"])))
#         # </editor-fold>
#
#         webpage = render_template("top10.html", idnr=idnr, top10_list=top10_list, user_name=user_name)
#         return webpage
#     except Exception as e:
#         webpage = render_template("ErrorPageView.html", function="suggestion_page(idnr)", error_type=str(type(e)),
#                                   error=str(e))
#         return webpage
#
#
# @app.route("/billboard/<idnr>")
# def billboard_page(idnr):
#     try:
#
#         # <editor-fold desc="MongoDB query">
#         user_name: List[str] = list(map(
#             lambda users: users["name"],
#             mongo_db_api.query_user_db({"id": idnr}, {"name": 1})
#         ))[0]
#
#         billboard_list: List[Track] = list(mongo_db_api.query_billboard_db({
#             "id": idnr
#         }, {
#             "name": 1,
#             "lastfm_url": 1,
#             "lastfm_listeners": 1,
#             "lastfm_playcount": 1,
#             "artist": 1,
#             "album": 1,
#             "album_creator": 1,
#         }).sort("lastfm_url", 1))
#         # </editor-fold>
#
#         # <editor-fold desc="List procesing">
#         billboard_list.sort(reverse=False, key=(lambda track: int(track["lastfm_url"])))
#         # </editor-fold>
#
#         webpage = render_template("billboard.html", idnr=idnr, billboard_list=billboard_list, user_name=user_name)
#         return webpage
#     except Exception as e:
#         webpage = render_template("ErrorPageView.html", function="suggestion_page(idnr)", error_type=str(type(e)),
#                                   error=str(e))
#         return webpage
#
#
# @app.route("/deleteAll")
# def delete_all_page():
#     try:
#
#         # <editor-fold desc="MongoDB delete">
#         mongo_db_api.delete_user_db({})
#         mongo_db_api.delete_artist_db({})
#         mongo_db_api.delete_music_db({})
#         # </editor-fold>
#
#         webpage = redirect(location="/", code=302)
#         return webpage
#     except Exception as e:
#         webpage = render_template("ErrorPageView.html", function="delete_all_page(idnr)", error_type=str(type(e)),
#                                   error=str(e))
#         return webpage


if __name__ == "__main__":
    app.run()

from flask import Flask, request, jsonify
import pprint

from Controller.EndpointController.MusicRecEPController import MusicRecEPController
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

lastfm_api: LastFmAPI = LastFmAPI()
mongodb_api: MongoDBAPI = MongoDBAPI()

# mongodb_api.delete_lastfm_db(delete={})
# for track in lastfm_api.get_lastfm_charts(10):
#     mongodb_api.update_lastfm_db(
#         selection=None,
#         update=track.json()
#     )

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


@app.route('/json/lastFMTop', methods=['GET'])
def last_fm_top_ep():
    last_fm_top_ep_controller: LastFMTopEPController = LastFMTopEPController()
    return jsonify(last_fm_top_ep_controller.json())


@app.route('/json/userTags/<fid>', methods=['GET'])
def user_tags_ep(fid):
    user_tags_ep_controller: UserTagsEPController = UserTagsEPController(fid)
    return jsonify(user_tags_ep_controller.json())


@app.route('/json/musicRec/<fid>', methods=['GET'])
def music_rec_ep(fid):
    music_rec_ep_controller: MusicRecEPController = MusicRecEPController(fid)
    return jsonify(music_rec_ep_controller.json())


if __name__ == "__main__":
    app.run()

from flask import Flask, request, jsonify
import pprint

from Controller.PageController.HomePageController import HomePageController
from Controller.PageController.StatusPageController import StatusPageController
from Controller.PageController.MusicPageController import MusicPageController
from Controller.PageController.MoviePageController import MoviePageController
from Controller.PageController.ErrorPageController import ErrorPageController
from Controller.EntryController.UserEntryController import UserEntryController
from Controller.EndpointController.LastFMChartsEPController import LastFMChartsEPController
from Controller.EndpointController.TheMovieDBChartsEPController import TheMovieDBChartsEPController
from Controller.EndpointController.UserTagsEPController import UserTagsEPController
from Controller.EndpointController.UserGenresEPController import UserGenresEPController
from Controller.EndpointController.MusicRecEPController import MusicRecEPController
from Controller.EndpointController.MovieRecEPController import MovieRecEPController

from APIs.MongoDBAPI import MongoDBAPI
from APIs.LastFmAPI import LastFmAPI
from APIs.TheMovieDBAPI import TheMovieDBAPI

mongodb_api: MongoDBAPI = MongoDBAPI()
lastfm_api: LastFmAPI = LastFmAPI()
themoviedb_api: TheMovieDBAPI = TheMovieDBAPI()

mongodb_api.delete_lastfm_db(delete={})
mongodb_api.delete_themoviedb_db(delete={})
for track in lastfm_api.get_lastfm_charts(nr=10):
    mongodb_api.update_lastfm_db(
        selection=None,
        update=track.json()
    )
for movie in themoviedb_api.get_themoviedb_charts(nr=10):
    mongodb_api.update_lastfm_db(
        selection=None,
        update=movie.json()
    )

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home_page():
    home_page_controller: HomePageController = HomePageController()
    return home_page_controller.render()


@app.route("/facebookLoginReply", methods=['GET'])
def facebook_login_reply_page():
    user_entry_controller: UserEntryController = UserEntryController(code=request.args.get("code"))
    return user_entry_controller.render()


@app.route("/Status/<fid>", methods=['GET'])
def status_page(fid):
    if fid == "alt=":
        return None
    else:
        status_page_controller: StatusPageController = StatusPageController(fid=fid)
        return status_page_controller.render()


@app.route("/Music/<fid>", methods=['GET'])
def music_page(fid):
    music_page_controller: MusicPageController = MusicPageController(fid=fid)
    return music_page_controller.render()


@app.route("/Movie/<fid>", methods=['GET'])
def movie_page(fid):
    movie_page_controller: MoviePageController = MoviePageController(fid=fid)
    return movie_page_controller.render()


@app.route("/Error/<fid>", methods=['GET'])
def error_page(fid):
    error_page_controller: ErrorPageController = ErrorPageController(fid=fid)
    return error_page_controller.render()


@app.route('/json/lastFMCharts', methods=['GET'])
def lastfm_charts_ep():
    lastfm_charts_ep_controller: LastFMChartsEPController = LastFMChartsEPController()
    return jsonify(lastfm_charts_ep_controller.json())


@app.route('/json/theMovieDBCharts', methods=['GET'])
def themoviedb_charts_ep():
    themoviedb_charts_ep_controller: TheMovieDBChartsEPController = TheMovieDBChartsEPController()
    return jsonify(themoviedb_charts_ep_controller.json())


@app.route('/json/userTags/<fid>', methods=['GET'])
def user_tags_ep(fid):
    user_tags_ep_controller: UserTagsEPController = UserTagsEPController(fid=fid)
    return jsonify(user_tags_ep_controller.json())


@app.route('/json/userGenres/<fid>', methods=['GET'])
def user_genres_ep(fid):
    user_genres_ep_controller: UserGenresEPController = UserGenresEPController(fid=fid)
    return jsonify(user_genres_ep_controller.json())


@app.route('/json/musicRec/<fid>', methods=['GET'])
def music_rec_ep(fid):
    music_rec_ep_controller: MusicRecEPController = MusicRecEPController(fid=fid)
    return jsonify(music_rec_ep_controller.json())


@app.route('/json/movieRec/<fid>', methods=['GET'])
def movie_rec_ep(fid):
    movie_rec_ep_controller: MovieRecEPController = MovieRecEPController(fid=fid)
    return jsonify(movie_rec_ep_controller.json())


if __name__ == "__main__":
    app.run()

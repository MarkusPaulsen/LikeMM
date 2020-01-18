# <editor-fold desc="Libaries">
from typing import *
import pymongo
import os
# </editor-fold>


# noinspection PyUnresolvedReferences
class MongoDBAPI:

    # <editor-fold desc="Constructor">
    def __init__(self):
        self.mongo_pass: str = os.environ["mongo_pass"]
        self.mongo_db_client = pymongo.MongoClient("mongodb+srv://HiItsLuis:" + self.mongo_pass + "@fermovies-kdmcj.mongodb.net/test?retryWrites=true&w=majority")
        #self.mongo_db_client = pymongo.MongoClient("mongodb://localhost:27017/")
        if "SNLLAB1DB" in self.mongo_db_client.list_database_names():
            self.sn_lab1_db = self.mongo_db_client["SNLLAB1DB"]
        else:
            raise Exception("SNLLAB1DB cannot be found")
    # </editor-fold>

    # <editor-fold desc="User DB">
    def get_user_db(self) -> Optional[pymongo.collection.Collection]:
        try:
            if "User" in self.sn_lab1_db.list_collection_names():
                output: Optional[pymongo.collection.Collection] = self.sn_lab1_db["User"]
                return output
            else:
                return None
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def update_user_db(self, selection: Optional[dict], update: Optional[dict])\
            -> Optional[pymongo.results.InsertOneResult]:
        try:
            if update is None:
                return None
            else:
                if selection is None:
                    output: Optional[pymongo.results.InsertOneResult] = self.get_user_db().update_one(
                        update,
                        {"$set": update},
                        upsert=True
                    )
                else:
                    output: Optional[pymongo.results.InsertOneResult] = self.get_user_db().update_one(
                        selection,
                        {"$set": update},
                        upsert=False
                    )
                return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def delete_user_db(self, delete: dict):
        try:
            output = self.get_user_db().delete_many(
                delete
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def query_user_db(self, selection: Optional[dict], projection: Optional[dict]):
        try:
            if selection is None:
                if projection is None:
                    output = self.get_user_db().find()
                else:
                    output = self.get_user_db().find(
                        {},
                        selection
                    )
            else:
                if projection is None:
                    output = self.get_user_db().find(
                        selection
                    )
                else:
                    output = self.get_user_db().find(
                        selection,
                        projection
                    )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None
    # </editor-fold>

    # <editor-fold desc="Artist DB">
    def get_artist_db(self) -> Optional[pymongo.collection.Collection]:
        try:
            if "Artist" in self.sn_lab1_db.list_collection_names():
                output: Optional[pymongo.collection.Collection] = self.sn_lab1_db["Artist"]
                return output
            else:
                return None
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def update_artist_db(self, selection: Optional[dict], update: Optional[dict])\
            -> Optional[pymongo.results.InsertOneResult]:
        try:
            if update is None:
                return None
            else:
                if selection is None:
                    output: Optional[pymongo.results.InsertOneResult] = self.get_artist_db().update_one(
                        update,
                        {"$set": update},
                        upsert=True
                    )
                else:
                    output: Optional[pymongo.results.InsertOneResult] = self.get_artist_db().update_one(
                        selection,
                        {"$set": update},
                        upsert=False
                    )
                return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def delete_artist_db(self, delete: dict):
        try:
            output = self.get_artist_db().delete_many(
                delete
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def query_artist_db(self, selection: Optional[dict], projection: Optional[dict]):
        try:
            if selection is None:
                if projection is None:
                    output = self.get_artist_db().find()
                else:
                    output = self.get_artist_db().find(
                        {},
                        selection
                    )
            else:
                if projection is None:
                    output = self.get_artist_db().find(
                        selection
                    )
                else:
                    output = self.get_artist_db().find(
                        selection,
                        projection
                    )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    # </editor-fold>

    # <editor-fold desc="Movie DB">
    def get_movie_db(self) -> Optional[pymongo.collection.Collection]:
        try:
            if "Movie" in self.sn_lab1_db.list_collection_names():
                output: Optional[pymongo.collection.Collection] = self.sn_lab1_db["Movie"]
                return output
            else:
                return None
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def update_movie_db(self, selection: Optional[dict], update: Optional[dict])\
            -> Optional[pymongo.results.InsertOneResult]:
        try:
            if update is None:
                return None
            else:
                if selection is None:
                    output: Optional[pymongo.results.InsertOneResult] = self.get_movie_db().update_one(
                        update,
                        {"$set": update},
                        upsert=True
                    )
                else:
                    output: Optional[pymongo.results.InsertOneResult] = self.get_movie_db().update_one(
                        selection,
                        {"$set": update},
                        upsert=False
                    )
                return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def delete_movie_db(self, delete: dict):
        try:
            output = self.get_movie_db().delete_many(
                delete
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def query_movie_db(self, selection: Optional[dict], projection: Optional[dict]):
        try:
            if selection is None:
                if projection is None:
                    output = self.get_movie_db().find()
                else:
                    output = self.get_movie_db().find(
                        {},
                        selection
                    )
            else:
                if projection is None:
                    output = self.get_movie_db().find(
                        selection
                    )
                else:
                    output = self.get_movie_db().find(
                        selection,
                        projection
                    )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    # </editor-fold>

    # <editor-fold desc="LastFM DB">
    def get_lastfm_db(self) -> Optional[pymongo.collection.Collection]:
        try:
            if "LastFM" in self.sn_lab1_db.list_collection_names():
                output: Optional[pymongo.collection.Collection] = self.sn_lab1_db["LastFM"]
                return output
            else:
                return None
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def update_lastfm_db(self, selection: Optional[dict], update: Optional[dict])\
            -> Optional[pymongo.results.InsertOneResult]:
        try:
            if update is None:
                return None
            else:
                if selection is None:
                    output: Optional[pymongo.results.InsertOneResult] = self.get_lastfm_db().update_one(
                        update,
                        {"$set": update},
                        upsert=True
                    )
                else:
                    output: Optional[pymongo.results.InsertOneResult] = self.get_lastfm_db().update_one(
                        selection,
                        {"$set": update},
                        upsert=False
                    )
                return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def delete_lastfm_db(self, delete: dict):
        try:
            output = self.get_lastfm_db().delete_many(
                delete
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def query_lastfm_db(self, selection: Optional[dict], projection: Optional[dict]):
        try:
            if selection is None:
                if projection is None:
                    output = self.get_lastfm_db().find()
                else:
                    output = self.get_lastfm_db().find(
                        {},
                        selection
                    )
            else:
                if projection is None:
                    output = self.get_lastfm_db().find(
                        selection
                    )
                else:
                    output = self.get_lastfm_db().find(
                        selection,
                        projection
                    )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None
    # </editor-fold>

    # <editor-fold desc="TheMovieDB DB">
    def get_themoviedb_db(self) -> Optional[pymongo.collection.Collection]:
        try:
            if "TheMovieDB" in self.sn_lab1_db.list_collection_names():
                output: Optional[pymongo.collection.Collection] = self.sn_lab1_db["TheMovieDB"]
                return output
            else:
                return None
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def update_themoviedb_db(self, selection: Optional[dict], update: Optional[dict]) \
            -> Optional[pymongo.results.InsertOneResult]:
        try:
            if update is None:
                return None
            else:
                if selection is None:
                    output: Optional[pymongo.results.InsertOneResult] = self.get_themoviedb_db().update_one(
                        update,
                        {"$set": update},
                        upsert=True
                    )
                else:
                    output: Optional[pymongo.results.InsertOneResult] = self.get_themoviedb_db().update_one(
                        selection,
                        {"$set": update},
                        upsert=False
                    )
                return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def delete_themoviedb_db(self, delete: dict):
        try:
            output = self.get_themoviedb_db().delete_many(
                delete
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def query_themoviedb_db(self, selection: Optional[dict], projection: Optional[dict]):
        try:
            if selection is None:
                if projection is None:
                    output = self.get_themoviedb_db().find()
                else:
                    output = self.get_themoviedb_db().find(
                        {},
                        selection
                    )
            else:
                if projection is None:
                    output = self.get_themoviedb_db().find(
                        selection
                    )
                else:
                    output = self.get_themoviedb_db().find(
                        selection,
                        projection
                    )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None
    # </editor-fold>

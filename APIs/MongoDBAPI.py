# <editor-fold desc="Libaries">
from typing import *
import pymongo
# </editor-fold>


# noinspection PyMethodMayBeStatic
class MongoDBAPI:

    # <editor-fold desc="Constructor">
    def __init__(self):
        self.mongo_db_client = pymongo.MongoClient("mongodb://localhost:27017/")
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

    def insert_user_db(self, entry_to_insert: dict) -> Optional[pymongo.results.InsertOneResult]:
        try:
            output: Optional[pymongo.results.InsertOneResult] = self.get_user_db().update_one(
                entry_to_insert,
                {"$set": entry_to_insert},
                upsert=True
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def delete_user_db(self, entry_to_delete: dict):
        try:
            output = self.get_user_db().delete_many(
                entry_to_delete
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def query_user_db(self, selection: dict, projection: dict):
        try:
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

        def insert_artist_db(self, entry_to_insert: dict) -> Optional[pymongo.results.InsertOneResult]:
            try:
                output: Optional[pymongo.results.InsertOneResult] = self.get_artist_db().update_one(
                    entry_to_insert,
                    {"$set": entry_to_insert},
                    upsert=True
                )
                return output
            except Exception as e:
                print(type(e))
                print(e.args)
                print(e)
                return None

        def delete_artist_db(self, entry_to_delete: dict):
            try:
                output = self.get_artist_db().delete_many(
                    entry_to_delete
                )
                return output
            except Exception as e:
                print(type(e))
                print(e.args)
                print(e)
                return None

        def query_artist_db(self, selection: dict, projection: dict):
            try:
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

        def insert_artist_db(self, entry_to_insert: dict) -> Optional[pymongo.results.InsertOneResult]:
            try:
                output: Optional[pymongo.results.InsertOneResult] = self.get_artist_db().update_one(
                    entry_to_insert,
                    {"$set": entry_to_insert},
                    upsert=True
                )
                return output
            except Exception as e:
                print(type(e))
                print(e.args)
                print(e)
                return None

        def delete_artist_db(self, entry_to_delete: dict):
            try:
                output = self.get_artist_db().delete_many(
                    entry_to_delete
                )
                return output
            except Exception as e:
                print(type(e))
                print(e.args)
                print(e)
                return None

        def query_artist_db(self, selection: dict, projection: dict):
            try:
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

    # <editor-fold desc="Music DB">
    def get_music_db(self) -> Optional[pymongo.collection.Collection]:
        try:
            if "Music" in self.sn_lab1_db.list_collection_names():
                output = self.sn_lab1_db["Music"]
                return output
            else:
                return None
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def insert_music_db(self, entry_to_insert: dict) -> Optional[pymongo.results.InsertOneResult]:
        try:
            output: Optional[pymongo.results.InsertOneResult] = self.get_music_db().update_one(
                entry_to_insert,
                {"$set": entry_to_insert},
                upsert=True
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def delete_music_db(self, entry_to_delete: dict):
        try:
            output = self.get_music_db().delete_many(
                entry_to_delete
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def query_music_db(self, selection: dict, projection: dict):
        try:
            output = self.get_music_db().find(
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

    # <editor-fold desc="Top10 DB">
    def get_top10_db(self) -> Optional[pymongo.collection.Collection]:
        try:
            if "Top10" in self.sn_lab1_db.list_collection_names():
                output = self.sn_lab1_db["Top10"]
                return output
            else:
                return None
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def insert_top10_db(self, entry_to_insert: dict) -> Optional[pymongo.results.InsertOneResult]:
        try:
            output: Optional[pymongo.results.InsertOneResult] = self.get_top10_db().update_one(
                entry_to_insert,
                {"$set": entry_to_insert},
                upsert=True
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def delete_top10_db(self, entry_to_delete: dict):
        try:
            output = self.get_top10_db().delete_many(
                entry_to_delete
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def query_top10_db(self, selection: dict, projection: dict):
        try:
            output = self.get_top10_db().find(
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

    # <editor-fold desc="Billboard DB">
    def get_billboard_db(self) -> Optional[pymongo.collection.Collection]:
        try:
            if "Billboard" in self.sn_lab1_db.list_collection_names():
                output = self.sn_lab1_db["Billboard"]
                return output
            else:
                return None
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def insert_billboard_db(self, entry_to_insert: dict) -> Optional[pymongo.results.InsertOneResult]:
        try:
            output: Optional[pymongo.results.InsertOneResult] = self.get_billboard_db().update_one(
                entry_to_insert,
                {"$set": entry_to_insert},
                upsert=True
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def delete_billboard_db(self, entry_to_delete: dict):
        try:
            output = self.get_billboard_db().delete_many(
                entry_to_delete
            )
            return output
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)
            return None

    def query_billboard_db(self, selection: dict, projection: dict):
        try:
            output = self.get_billboard_db().find(
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

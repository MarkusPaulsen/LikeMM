from APIs.MongoDBAPI import MongoDBAPI


class UserTagsEPController:

    def __init__(self,fid):
        self.fid = fid
        self.mongo_db_api: MongoDBAPI = MongoDBAPI()
        self.user_data = None
        self.artist_list = None
        self.tag_list = None

    def load_user_data(self):
        self.user_data = list(self.mongo_db_api.query_user_db({
            "id": self.fid
        }, {
            "music": 1
        }))[0]

    def generate_tag_list(self):
        self.artist_list = list(map(
            lambda entry: entry["name"],
            self.user_data["music"]["data"]
        ))

    def generate_tag_list(self):
        self.tag_list = list(map())

    def json(self):
        pass

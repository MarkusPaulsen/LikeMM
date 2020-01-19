from APIs.MongoDBAPI import MongoDBAPI


class UserTagsEPController:

    def __init__(self, fid):
        self.fid = fid
        self.mongodb_api: MongoDBAPI = MongoDBAPI()
        self.tag_list = []

    def load_tag_list(self):
        query_element = list(self.mongodb_api.query_artist_db(
            selection={"id": self.fid},
            projection={"lastfm_tags": 1}
        ))
        tag_list_of_lists = list(map(lambda tag_list: [tag_list["lastfm_tags"][0]], query_element))
        tag_list_not_unique = [tag for tag_list in tag_list_of_lists for tag in tag_list]
        self.tag_list = list(set(tag_list_not_unique))

    def json(self):
        self.load_tag_list()
        return self.tag_list

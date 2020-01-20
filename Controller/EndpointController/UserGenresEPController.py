from APIs.MongoDBAPI import MongoDBAPI


class UserGenresEPController:

    def __init__(self, fid):
        self.fid = fid
        self.mongodb_api: MongoDBAPI = MongoDBAPI()
        self.genre_list = []

    def get_first_element(self, element_list):
        try:
            return [element_list[0]]
        except Exception:
            return []

    def load_genre_list(self):
        query_element = list(self.mongodb_api.query_movie_db(
            selection={"id": self.fid},
            projection={"themoviedb_genres": 1}
        ))
        genre_list_of_lists = list(map(
            lambda genre_list: self.get_first_element(genre_list["themoviedb_genres"]),
            query_element
        ))
        genre_list_not_unique = [genre for genre_list in genre_list_of_lists for genre in genre_list]
        self.genre_list = list(set(genre_list_not_unique))

    def json(self):
        self.load_genre_list()
        return self.genre_list

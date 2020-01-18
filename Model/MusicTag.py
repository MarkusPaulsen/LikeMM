class MusicTag:

    # <editor-fold desc="Constructor">
    def __init__(self, lastfm_input: dict):
        self.name: str = lastfm_input["name"]

    def json(self):
        return self.name
    # </editor-fold>

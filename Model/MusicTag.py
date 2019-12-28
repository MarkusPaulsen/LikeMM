class MusicTag:

    # <editor-fold desc="Constructor">
    def __init__(self, input_data: dict):
        self.name: str = input_data["name"]
        self.lastfm_url: str = input_data["url"]
    # </editor-fold>

class User:

    # <editor-fold desc="Constructor">
    def __init__(self, input_data: dict):
        self.id: str = input_data["id"]
        self.name: str = input_data["name"]
        self.email: str = input_data["email"]
    # </editor-fold>

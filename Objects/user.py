

class User:

    def __init__(self, key: str, secret: str, user_id: int):
        self.__key = key
        self.__secret = secret
        self.__user_id = user_id

    def set_user_params(self):
        return {"id": self.__user_id, "key": self.__key}

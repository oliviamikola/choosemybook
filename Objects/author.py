from collections import OrderedDict


class Author:

    def __init__(self, author_data: OrderedDict):
        """
        Initializes an instance of an author
        :param author_data: ordered dictionary of author data from goodreads
        """
        self._author_id = author_data["id"]
        self._name = author_data["name"]
        self._goodreads_link = author_data["link"]
        self._rating = author_data["average_rating"]
        self._ratings_count = author_data["ratings_count"]

    def __str__(self) -> str:
        """
        Formats the author object
        :return: string with Author data
        """
        return "{} (ID: {})".format(self._name, self._author_id)

from collections import OrderedDict


class Author:

    def __init__(self, author_data: OrderedDict):
        """
        Initializes an instance of an author
        :param author_data: ordered dictionary of author data from goodreads
        """
        self.author_id = author_data["id"]
        self.name = author_data["name"]
        self.goodreads_link = author_data["link"]
        self.rating = author_data["average_rating"]
        self.ratings_count = author_data["ratings_count"]

    def __str__(self):
        """
        Formats the author object
        :return: string with Author data
        """
        return "{} (ID: {})".format(self.name, self.author_id)

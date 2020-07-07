from collections import OrderedDict
from Objects.author import Author


class Book:

    def __init__(self, book_data: OrderedDict):
        """
        Initializes an instance of a book
        :param book_data: ordered dictionary of book data received from goodreads
        """
        self._book_id = book_data["id"]["#text"]
        self._title = book_data["title"]
        self._title_without_series = book_data["title_without_series"]
        self._author = Author(book_data["authors"]["author"])
        self._goodreads_link = book_data["link"]
        self._pages = book_data["num_pages"]
        self._description = book_data["description"]
        self._isbn = book_data["isbn"]

    def __str__(self) -> str:
        """
        Formats the book object
        :return: string with Book data
        """
        return "{} (ID: {}) \nBy: {}".format(self._title, self._book_id, self._author)

    def get_id(self) -> str:
        """
        Gets the ID of the given book
        :return: ID of book
        """
        return self._book_id

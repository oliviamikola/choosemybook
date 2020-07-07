from collections import OrderedDict
from author import Author


class Book:

    def __init__(self, book_data: OrderedDict):
        """
        Initializes an instance of a book
        :param book_data: ordered dictionary of book data received from goodreads
        """
        self.book_id = book_data["id"]["#text"]
        self.title = book_data["title"]
        self.title_without_series = book_data["title_without_series"]
        self.author = Author(book_data["authors"]["author"])
        self.goodreads_link = book_data["link"]
        self.pages = book_data["num_pages"]
        self.description = book_data["description"]
        self.isbn = book_data["isbn"]

    def __str__(self) -> str:
        """
        Formats the book object
        :return: string with Book data
        """
        return "{} (ID: {}) \nBy: {}".format(self.title, self.book_id, self.author)

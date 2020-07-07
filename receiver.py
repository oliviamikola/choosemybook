import requests
import time
import xmltodict
from book import Book


class Receiver:

    def __init__(self, key, secret, user_id):
        """
        Initializes important user data to collect book data
        :param key: API key specific to the user
        :param secret: secret that is made with API key
        :param user_id: user ID linked with their GoodReads account
        """
        self.key = key
        self.secret = secret
        self.user_id = user_id

    def collect_books(self, shelf="to-read"):
        """
        Collects the books from the given shelf
        :param shelf: shelf to get books from
        :return: dictionary containing books from shelf
        """
        url = "https://www.goodreads.com/review/list"
        params = {"v": 2, "id": self.user_id, "shelf": shelf, "key": self.key, "page": 1, "per_page": 200}

        # Must have 1 second between requests
        current_time = time.time()

        # Will contain all books on the shelf and their data
        books_on_shelf = {}

        while True:
            r = requests.get(url, params=params)

            # Getting the number of books on the shelf and the last one received
            book_stats = r.text.split("\n")[10].split('"')
            total_books = book_stats[5]
            last_book_in_list = book_stats[3]

            this_get_books = xmltodict.parse(r.text)["GoodreadsResponse"]["reviews"]["review"]

            # Get the essential data about the book and put it into a dictionary
            for book in this_get_books:
                book_data = book["book"]
                book_id = book_data["id"]["#text"]  # goodreads already has unique keys for each book
                books_on_shelf[book_id] = Book(book_data)  # Note: book_id is kept as a string

            # We have all the books
            if total_books == last_book_in_list:
                break

            params["page"] += 1

            # goodreads API usage rules
            while time.time() - current_time < 1.0:
                pass
            current_time = time.time()

        return books_on_shelf

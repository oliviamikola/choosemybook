import requests
import time
import xmltodict
from typing import Dict
from book import Book
from user import User


class Receiver:

    def __init__(self, user: User):
        """
        Initializes important user data to collect book data
        :param user: The user whose data is being collected
        """
        self.user = user
        self.last_checked_time = time.time()

    def collect_books(self, shelf: str = "to-read") -> Dict[str, Book]:
        """
        Collects the books from the given shelf
        :param shelf: shelf to get books from
        :return: dictionary containing books from shelf
        """
        url = "https://www.goodreads.com/review/list"
        params = {**{"v": 2, "shelf": shelf, "page": 1, "per_page": 200}, **(self.user.set_user_params())}

        self.__update_time()

        # Will contain all books on the shelf and their data
        books_on_shelf = {}

        while True:
            goodreads_data = self.__retry(url, params)

            # Getting the number of books on the shelf and the last one received
            book_stats = goodreads_data.split("\n")[10].split('"')
            total_books = book_stats[5]
            last_book_in_list = book_stats[3]

            self.__translate_data(goodreads_data, books_on_shelf)

            # Check if all the books are accounted for
            if total_books == last_book_in_list:
                break

            params["page"] += 1

            self.__keep_time()

        return books_on_shelf

    def __keep_time(self) -> None:
        """
        Ensures goodreads API usage rules are followed
        :return: None
        """
        while time.time() - self.last_checked_time < 1.0:
            pass
        self.__update_time()

    def __update_time(self) -> None:
        """
        Updates the last checked time
        :return: None
        """
        self.last_checked_time = time.time()

    def __retry(self, url: str, params: Dict[str, object]) -> str:
        """
        Attempts data collection from goodreads
        Raises an error if unable to connect
        :param url: request url
        :param params: params required to get goodreads data
        :return: received data if successful, otherwise raises error
        """
        for _ in range(5):
            self.__update_time()
            request = requests.get(url, params=params)
            if request.status_code == 200:
                return request.text
            self.__keep_time()
        else:
            raise ValueError  # TODO: Make custom error

    def __translate_data(self, goodreads_data: str, books_on_shelf: Dict[str, Book]) -> None:
        """
        Translates goodreads data from received XML to a dictionary of Book objects
        :param goodreads_data: data received from goodreads API call
        :param books_on_shelf: dictionary containing Book objects
        :return: None
        """
        dict_data = xmltodict.parse(goodreads_data)["GoodreadsResponse"]["reviews"]["review"]

        # Get essential data about the book and add to dictionary
        for book_data in dict_data:
            book_data = book_data["book"]
            book = Book(book_data)
            books_on_shelf[book.book_id] = book

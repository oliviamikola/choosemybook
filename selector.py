import random
from typing import Optional, Dict
from Objects.book import Book


class Selector:

    def __init__(self, book_dict: Dict[str, Book]):
        """
        Initializes the selector
        :param book_dict: dictionary of books gathered from receiver
        """
        self.book_dict = book_dict
        self.number = len(self.book_dict)

    def select_book(self) -> Optional[Book]:
        """
        Randomly selects a book from book_dict
        :return: the selected book
        """
        if self.number == 0:
            return None

        book_ids = list(self.book_dict.keys())
        random.shuffle(book_ids)
        book_id = book_ids[0]
        book = self.book_dict[book_id]
        return book

import random


class Selector:

    def __init__(self, book_dict):
        """
        Initializes the selector
        :param book_dict: dictionary of books gathered from receiver
        """
        self.book_dict = book_dict
        self.number = len(self.book_dict)

    def select_book(self):
        chosen = random.randint(1, 62)
        count = 1
        if self.number == 0:
            return None
        for book_id in self.book_dict:
            if count == chosen:
                return self.book_dict[book_id]
            count += 1

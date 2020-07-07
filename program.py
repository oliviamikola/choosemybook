from receiver import Receiver
from selector import Selector
from Objects.user import User


def main():
    user_data = input().split()
    user = User(user_data[0], user_data[1], int(user_data[2]))

    book_data = Receiver(user).collect_books()
    chosen_book = Selector(book_data).select_book()

    print(chosen_book)


if __name__ == "__main__":
    main()

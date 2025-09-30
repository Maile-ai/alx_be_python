class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

class Library:
    def __init__(self):
        self.__books = []
    def add_book(self, book):
            self.__books.append(book)
    def check_out_book(self, book):
            if book in self.__books and not book._Book__is_checked_out:
                book._Book__is_checked_out = True
                return True
            return False
    def return_book(self, book):
            if book in self.__books and book._Book__is_checked_out:
                book._Book__is_checked_out = False
                return True
            return False
    def list_available_books(self):
            return [book for book in self.__books if not book._Book__is_checked_out]
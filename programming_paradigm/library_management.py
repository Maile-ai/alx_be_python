class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False  # private attribute

    def is_checked_out(self):
        return self.__is_checked_out

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
            self._books.append(book)
    def check_out_book(self, book):
            if book in self._books and not book._Book__is_checked_out:
                book._Book__is_checked_out = True
                return True
            return False
    def return_book(self, book):
            if book in self._books and book._Book__is_checked_out:
                book._Book__is_checked_out = False
                return True
            return False
    def list_available_books(self):
            return [book for book in self._books if not book._Book__is_checked_out]
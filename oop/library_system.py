class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        # This is the human-readable representation
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):
        # Override Book's __str__ to include file size
        return f"E-Book: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.num_pages = page_count

    def __str__(self):
        # Override Book's __str__ to include page count
        return f"Print Book: {self.title} by {self.author}, Pages: {self.num_pages}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)  # Calls the __str__() of each book type
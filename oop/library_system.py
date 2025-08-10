# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def details(self):
        return f"Book: {self.title} by {self.author}"


# Derived class for EBooks
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size  # in KB

    def details(self):
        return f"EBook: {self.title} by {self.author} File Size: {self.file_size} KB"


# Derived class for Print Books
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count

    def details(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Library class demonstrating composition
class Library:
    def __init__(self):
        self.books = []  # List to store books

    def add_book(self, book):
        if isinstance(book, Book):  # Ensure only Book or subclasses are added
            self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.details())

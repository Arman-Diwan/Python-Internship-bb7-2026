class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, title):
        self.__books.append(title)
        print(title, "added successfully")

    def remove_book(self, title):
        if title in self.__books:
            self.__books.remove(title)
            print(title, "removed successfully")
        else:
            print("Book not found")

    def list_books(self):
        print("Available Books:")
        for book in self.__books:
            print(book)


library = Library()

library.add_book("Python Programming")
library.add_book("Java Programming")
library.add_book("Web Development")

library.list_books()

library.remove_book("Java Programming")

library.list_books()
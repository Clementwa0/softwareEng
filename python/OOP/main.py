from library import Library
from book import Book
from magazine import Magazine
from digitalbook import DigitalBook


def main():

    library.add_book(Book("Atomic Habits", "James Clear", 2018))
    library.add_book(Book("Deep Work", "Cal Newport", 2016))    
    library.add_book(Magazine("National Geographic", "John Doe", 2020))
    library.add_book(DigitalBook("Python Programming", "Jane Smith", 2021, 5.0))

    while True:
        print("Welcome to the Library!")
        print("1. List all books")
        print("2. Find a book")
        print("3. Borrow a book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Library Catalog:")
            for book in library.books:
                print("\n", book.get_details())
        elif choice == '2':
            title = input("Enter the title of the book: ")
            book = library.find_book(title)
            if book:
                print(book.get_details())
            else:
                print("Book not found.")
        elif choice == '3':
            title = input("Enter the title of the book to borrow: ")
            book = library.find_book(title)
            if book:
                print(book.borrow())
            else:
                print("Book not found.")
        elif choice == '4':
            print("Exiting the library. Goodbye!")
            break
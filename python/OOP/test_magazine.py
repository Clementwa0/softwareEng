from magazine import Magazine
from book import Book
from library import Library
lib = Library("Test Library")
lib.add_book(Magazine("National Geographic", "John Doe", 2020))
lib.add_book(Magazine("TIME", "Jane Smith", 2021))
lib.add_book(Magazine("Vogue", "Anna Wintour", 2019))

print("Library Catalog:")
for book in lib.list_books():
    print("\n", book)
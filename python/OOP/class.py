class Myclass:
    x = 5

# object 

p1 = Myclass()
print(p1.x)

class Library:
    def _init_(self, name):
    #create a new Library with a neme and empty list of book

        self.name = name
        self.books = []
    def add_book(self, book):
        """
        Add a book to the library collection
        """
        self.books.append(book)
    def list_books(self):
        """
        List all books in the library
        """
        return[book.get_details() for book in self.books] #fetch data in iterable format
        
    def find_book(self, title):
        """
        Find a book in the library by title
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
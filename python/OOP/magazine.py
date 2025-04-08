from book import Book

class Magazine(Book):
    def __init__(self, title, editor, year):
        """
        Constructor method to initialize the magazine object
        """
        super().__init__(title, editor, year)  # using super() to inherit the attributes from the book class

    def borrow(self):
        """
        Overrides the borrow method to indicate that magazines can't be borrowed.
        """
        return f"'{self.title}' is a magazine and can't be borrowed."
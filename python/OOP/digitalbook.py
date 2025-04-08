from book import Book

class DigitalBook(Book):
    def _init_(self,title, author, year, file_size):
            """
            Constructor method to initialize the digital book object
            """
            super()._init_(title, author, year) #using supper() to inherite the attributes from the book class
            self.file_size = file_size

    def stream(self):
        """
        Simulates streaming the digital book.
        """
        return f"Streaming '{self.title}' of size :{self.file_size}MB."
    
    def borrow(self):
        """
        Overrides the borrow method to indicate that digital books can be streamed.
        """
        return f"{self.title} is a digital book and can be streamed online."
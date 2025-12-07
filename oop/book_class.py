class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(book):
        return f"{book.title} by {book.author}, published in {book.year}"
    
    def __repr__(book):
        return f"Book('{book.title}', '{book.author}', '{book.year}')"
    
    def __del__(book):
        print(f"Deleting {book.title}")
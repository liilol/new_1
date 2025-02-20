class Book :
    def __init__(self, title, author, isbn, available  = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    
    def __str__(self):
        if self.available:
            print(f"{self.title} by {self.author} (ISBN: {self.isbn}) - Available")
        else:
            print(f"{self.title} by {self.author} (ISBN: {self.isbn}) - Checked Out")



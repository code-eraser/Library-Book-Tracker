class Book:
    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.is_available = True
        self.borrowed_by = None

    def borrow(self, member_id):
        if self.is_available:
            self.is_available = False
            self.borrowed_by = member_id
            return True
        return False
    def return_book(self):
        self.is_available = True
        self.borrowed_by = None
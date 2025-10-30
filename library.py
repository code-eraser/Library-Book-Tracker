from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, title, author, genre, isbn):
        self.books.append(Book(title, author, isbn, genre))
    
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    def find_member(self,member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    def borrow_book(self, isbn, member_id):
        book = self.find_book(isbn)
        member = self.find_member(member_id)
        if book and member and book.is_available:
            book.borrow(member_id)
            member.borrow_book(book)
            print(f"{member.name} borrowed '{book.title}'.")
        else:
            print("Book not available or member not found.")
    
    def return_book(self, isbn, member_id):
        book = self.find_book(isbn)
        member = self.find_member(member_id)
        if book and member and isbn in member.borrowed_books:
            book.return_book()
            member.return_book(book)
            print(f"{member.name} returned '{book.title}'.")
        else:
            print("Invalid operation.")
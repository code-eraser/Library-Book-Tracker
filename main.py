from library import Library

def main():
    lib = Library()

    while True:
        print("|n==== Library Menu ====")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Show All Books")
        print("6. Exit")
        choice = input("Enter Choice: ")
        
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            genre = input("Genre: ")
            lib.add_book(title,author,genre,isbn)
            print("Book added successfully!")

        elif choice == "2":
            member_id = input("Enter Member_id: ")
            name = input("Input: ")
            lib.add_member(member_id, name)

        elif choice == "3":
            isbn =input("Enter ISBN of the book you are borrowing: ")
            member_id = input("Enter your member_id: ")
            lib.borrow_book(isbn,member_id)
        elif choice == "4":
            isbn =input("Enter ISBN of the book you are returning: ")
            member_id = input("Enter your member_id: ")
            lib.return_book(isbn,member_id)
        
        elif choice == "5":
            print("\nAll Books:")
            for book in lib.books:
                status = "Available" if book.is_available else f"Borrowed by {book.borrowed_by}"
                print(f"{book.title} by {book.author} - {status}")

        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
    
if __name__ == "__main__":
    main()
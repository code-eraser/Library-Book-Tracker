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
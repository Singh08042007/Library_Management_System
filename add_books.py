from utils import books
def add():
    book_name = input("Enter the Book name to add: ").upper().strip()

    if book_name in books:
        books[book_name] += 1
    else:
        books[book_name] = 1

    print(f"Book Added: {book_name}")
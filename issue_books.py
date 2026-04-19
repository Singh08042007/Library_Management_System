from utils import books,issue_books
def issue():
    book_name=input("Enter the book name to issue: ").upper()
    if book_name in books and books[book_name] > 0:
        books[book_name] -= 1
        issue_books.append(book_name)
        print("Book assigned successfully")
    else:
        print("Book not available")
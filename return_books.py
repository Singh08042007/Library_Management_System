from utils import books,issue_books
def return_book():
    book_name=input("Enter the book name to return: ").upper()
    if book_name in issue_books:
        issue_books.remove(book_name)
        if book_name in books:
            books[book_name] += 1
        else:
            books[book_name] = 1
        print("Book returned")
    else:
        print("Book not issued")
from utils import books, issue_books
from datetime import datetime

def issue():
    book_name = input("Enter the book name to issue: ").upper()

    if book_name in books and books[book_name] > 0:
        student_name = input("Enter student name: ").title()
        date_input = input("Enter issue date (DD-MM-YYYY): ")

        issue_date = datetime.strptime(date_input, "%d-%m-%Y")

        books[book_name] -= 1

        issue_books[book_name] = {
            "student": student_name,
            "date": issue_date
        }

        print(f"Book issued to {student_name}")
    else:
        print("Book not available")
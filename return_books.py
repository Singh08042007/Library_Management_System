from utils import books, issue_books
from datetime import datetime

def return_book():
    book_name = input("Enter the book name to return: ").upper()

    if book_name in issue_books:
        data = issue_books[book_name]
        student_name = data["student"]
        issue_date = data["date"]
        date_input = input("Enter return date (DD-MM-YYYY): ")
        return_date = datetime.strptime(date_input, "%d-%m-%Y")
        days = (return_date - issue_date).days
        fine = 0

        if days > 7:
            extra_days = days - 7
            for d in range(1, extra_days + 1):
                week = (d // 7) + 1
                rate = 10
                for i in range(1, week + 1):
                    rate *= i
                fine += rate
        print(f"\nStudent: {student_name}")
        print(f"Total Days: {days}")

        if fine > 0:
            print(f"Fine to pay: ₹{fine}")
        else:
            print("No fine")
        del issue_books[book_name]
        if book_name in books:
            books[book_name] += 1
        else:
            books[book_name] = 1
        print("Book returned successfully")
        
    else:
        print("Book not issued")
from utils import books
def show():
    if len(books)==0: print("No Books Available")
    else:
        for book, count in books.items():
            print(f"{book} : {count}")


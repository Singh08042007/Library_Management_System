from add_books import add
from show_books import show
from issue_books import issue
from return_books import return_book

def library():
    while True:
        print("------Welcome to Library------")
        print("\n1. Add Book")
        print("2. Show Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice ==1: add()
        elif choice ==2: show()
        elif choice ==3: issue()
        elif choice ==4: return_book()
        elif choice == 5:
            print("Thankyou")
            break
        else:
            print("Invalid Choice")

library()

from add_books import add
from show_books import show
from issue_books import issue
from return_books import return_book

def library():
    while True:
        print("\n------Welcome to Library------")
        print("\n LIBRARY RULES:")
        print("• First 7 days: No fine")
        print("• After 7 days, fine per day per book:")
        print("   Week 1 → ₹10/day/book")
        print("   Week 2 → ₹20/day/book")
        print("   Week 3 → ₹60/day/book")
        print("   Week 4 → ₹240/day/book")
        print("   (Fine increases weekly in factorial pattern)\n")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add()
        elif choice == 2:
            show()
        elif choice == 3:
            issue()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank you for using Library System")
            break
        else:
            print("Invalid Choice")

library()
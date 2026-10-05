

from MyLibrary import add_book
from MyLibrary import show_all_books
from MyLibrary import search_book 
from MyLibrary import remove_book, upcoming_books


def show_menu():
    print("""
========= { Library Menu } =========
1. Add a book
2. View all books
3. Search for a book
4. Remove a book
5. View upcoming books
6. Exit
========= ~~~~  *****  ~~~~ ========
""")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            show_all_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            upcoming_books()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1 to 6.")
# match case can be implemented too, but in previous projects i already did that
# so this time i wanted to try something new 


if __name__ == "__main__":
    main()



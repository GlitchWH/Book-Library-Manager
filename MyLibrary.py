
#   MyLibrary.py
#   Class and core functions for the Book Library


import json

class booktintro:
    def __init__(self, b_name, a_name, chaps, genre, b_vol):
        self.b_name = b_name
        self.a_name = a_name
        self.chaps = chaps
        self.genre = genre
        self.b_vol = b_vol

    def convertintodict(self):
        return {
            "Book Name": self.b_name,
            "Author Name": self.a_name,
            "No. of Book Chapters": self.chaps,
            "Book Genre": self.genre,
            "No. of Volume": self.b_vol
        }


mylibrary = []
filename = "Mylibrary.json"   # <-- changed extension, since it's JSON now


def add_book():
    b_name = input("Enter Book name: ")
    a_name = input("Enter author name: ")
    chaps = int(input("Enter No. of chapters in book: "))
    genre = input("Enter Book Genre: ")
    b_vol = int(input("Enter Book Volume: "))

    new_book = booktintro(b_name, a_name, chaps, genre, b_vol)
    mylibrary.append(new_book)
    print(f"'{b_name}' added to the library.")
    rewrite_file()


def show_all_books():
    if not mylibrary:
        print("The library is empty.")
        return
    for book in mylibrary:
        print(book.convertintodict())


def search_book():
    search_term = input("Enter Book Name you want to search: ").lower()
    found = False
    for book in mylibrary:
        if search_term in book.b_name.lower():
            print(book.convertintodict())
            found = True
    if not found:
        print("No match found.")


def remove_book():
    bookname = input("Enter book name that you want to remove: ").lower()
    found_book = None
    for book in mylibrary:
        if book.b_name.lower() == bookname:
            found_book = book
            break

    if found_book is None:
        print("No book found with that name.")
        return

    mylibrary.remove(found_book)
    print(f"Removed '{found_book.b_name}' from library.")
    rewrite_file()


def rewrite_file():
    """Overwrites the JSON file so it always matches the current library list."""
    books = [b.convertintodict() for b in mylibrary]
    with open(filename, "w") as file:
        json.dump(books, file, indent=4)


def load_books():
    """Reads Mylibrary.json and rebuilds mylibrary from it."""
    try:
        with open(filename, "r") as file:
            books = json.load(file)
    except FileNotFoundError:
        return   # no file yet, nothing to load
    except json.JSONDecodeError:
        return   # file exists but is empty or broken, start fresh

    for data in books:
        book = booktintro(
            data["Book Name"],
            data["Author Name"],
            data["No. of Book Chapters"],
            data["Book Genre"],
            data["No. of Volume"]
        )
        mylibrary.append(book)


def upcoming_books():
    print("=== { Upcoming Books } ===")
    print("""
1. Game of Lust
2. Thorns and Flowers
3. Skies Falling Apart
4. Merciful Death
5. Habits of Falcon
6. Humble Farmer
7. Death is not Punishment
8. Land of Fairies
9. Wish
10. Splendid Sunrises
11. Faith
12. Clouds of Fear
13. Fear Management
14. In the Winds
""")


# Load existing books the moment this file is imported.
load_books()
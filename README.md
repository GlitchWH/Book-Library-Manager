# Book-Library-Manager
Book Library Manager is a beginner-friendly Python project that lets users add, search, remove, and view books through an interactive menu. Each book is represented as an object with attributes like name, author, genre, chapter count, and volume number. The library's data is saved to a JSON file, so books persist across sessions the program automatically loads existing data on startup and updates the file every time the library changes.

This project was built as a hands-on exercise in applying object-oriented programming concepts — classes, methods, and object lists to a practical, file-based application.
## Features
* Add a book — create a new book entry with name, author, genre, chapter count, and volume
* View all books — display every book currently in the library
* Search for a book — find books by partial or full name match
* Remove a book — delete a book from the library by name
* Persistent storage — all data is saved to a JSON file and reloaded automatically on the next run
* Menu-driven interface — a continuous loop lets users perform multiple actions without restarting the program

## project structure
book-library-manager/
│
├── MyLibrary.py 

Core class and functions (add, search, remove, save, load)
├── menu.py             

Entry point — imports from MyLibrary.py and runs the menu
├── Mylibrary.json     

Auto-generated data file (created on first run)
└── README.md

## How it works
* The booktintro class defines a book object with five attributes and a method to convert it into a dictionary.
* MyLibrary.py holds all the logic: adding, searching, removing, and saving/loading books. It has no menu of its own, making it reusable as an imported module.
* menu.py imports the needed functions from MyLibrary.py and runs the interactive menu loop. This is the file you actually run.
* Every time the library changes (a book is added or removed), the JSON file is rewritten to stay in sync with the in-memory list.
* On startup, the program reads the JSON file (if it exists) and rebuilds the book list in memory, so previously saved books are available immediately.

## Getting started
Python 3.x (no external libraries needed — uses only the built-in json module)
Clone the repository:
   git clone https://github.com/GlitchWH/Book-Library-Manager.git

Navigate into the project folder:
cd Book-Library-Manager

Run the menu file
python menu.py

## Usage
<img width="410" height="257" alt="image" src="https://github.com/user-attachments/assets/cd0ae1a2-b5a1-439b-baa9-42538f4adb0e" />
<img width="442" height="200" alt="image" src="https://github.com/user-attachments/assets/13b30a2a-8bae-4294-bda6-d225e1c39521" />
<img width="966" height="116" alt="image" src="https://github.com/user-attachments/assets/f8942b75-daae-44fe-be51-b63a73323ce5" />
<img width="447" height="398" alt="image" src="https://github.com/user-attachments/assets/54b04a32-aba5-4e58-b695-a5a42fa80f68" />

## Future Improvements
* Add input validation (e.g., prevent empty book names or negative chapter counts)
* Add the ability to edit an existing book's details
* Add sorting or filtering by genre
* Package as a standalone executable (.exe) for non-technical users

## License

This project is licensed under the MIT License — see below for details.
## Author
Waqas Hussain
Feel free to connect or check out more of my projects on GitHub.














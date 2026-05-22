# Library Management System

A simple command-line Library Management System written in Python. It provides basic functionality to add books, issue books to users, return books, and list available or issued books. Data is stored in-memory using Python dictionaries.

## Prerequisites
- Python 3.8 or newer

## Quick Start
1. Open a terminal and navigate to the project directory.
2. Run the main program:

```bash
python main.py
```

The program uses simple text-based interaction. No external packages are required.

## Features
- Add new books to the library
- Issue books to users
- Return issued books
- List available and issued books

## Project Files
- `main.py` — Program entry point and CLI flow
- `add_books.py` — Logic to add books to the collection
- `issue_books.py` — Logic to issue books to users
- `return_books.py` — Logic to return books
- `show_books.py` — Logic to display available or issued books
- `utils.py` — In-memory data stores (`books` and `issue_books` dictionaries)

## Notes
- This implementation stores data only in memory; restarting the program will reset the library state.
- For persistence, integrate a simple file-based storage or a database.

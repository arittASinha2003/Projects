
# Library Management System

This Python program implements a basic Library Management System. It allows users to perform various operations such as adding books, removing books, lending books, returning books, searching books by title, author, or genre, listing available books, listing overdue books, and showing active users. The program interacts with the MySQL database to store information about users, books, and issued books.

## Prerequisites

- Python 3.x installed on the system. [Link](https://www.python.org/downloads/)
- MySQL server installed and running. [Link](https://dev.mysql.com/downloads/)
- Required Python packages: mysql-connector-python, tabulate, python-dotenv
- A database named ```library``` in MySQL. You can create a database bu running:
```
create database library
```

## Package Installation

Install the required packages to run this program

1 : MySQL Connector for Python (mysql-connector-python):

```python
pip install mysql-connector-python
```

This package allows Python programs to connect to MySQL databases and interact with them using SQL queries. It's an essential tool for working with MySQL databases from within Python applications.

2 : Tabulate:

```python
pip install tabulate
```

This package provides a convenient way to format tabular data in Python. It can convert lists of dictionaries or lists of lists into nicely formatted tables, which can be printed to the console or included in reports or documents.

## Usage

1 : Run the program using Python:

```python
python library_management_system.py
```

2 : Follow the on-screen menu to perform various operations.

## Features

- Add Book: Add a new book to the library database.
- Remove Book: Remove an existing book from the library database.
- Lend Book: Lend a book to a user. Checks if the user exists, if not, registers the user. Checks if the maximum limit of 3 books per user is reached.
- Return Book: Return a book that was previously lent. Updates the book availability and user's issued book count.
- List Available Books: Display a list of books that are currently available in the library.
- List Overdue Books: Display a list of books that are overdue, along with user information.
- Show Active Users: Display a list of users who have currently lent books.
- Exit: Terminate the program.

## Database Table Structures

There are three tables present in the database:

- users: Contains information about library users.
  - id (INT, Primary Key): User ID
  - name (VARCHAR): User name
  - email (VARCHAR, Unique): User email
  - issued_book_count (INT): Count of books currently issued to the user

- issuedbooks: Tracks books that are currently issued.
  - id (INT, Auto Increment, Primary Key): Issued Book ID
  - issued_book_title (VARCHAR): Title of the issued book
  - user_id (INT, Foreign Key): ID of the user to whom the book is issued
  - issue_date (DATE): Date when the book was issued
  - due_date (DATE): Due date for returning the book

- books: Contains information about books available in the library.
  - id (INT, Auto Increment, Primary Key): Book ID
  - title (VARCHAR): Title of the book
  - author (VARCHAR): Author of the book
  - genre (VARCHAR): Genre of the book
  - available (BOOLEAN): Availability status of the book
  - user_id (INT, Foreign Key): ID of the user to whom the book is currently lent (NULL if available)

📚 Library Management System (Python OOP)
📌 Project Overview
This project is a Minimal Library Management System developed using Python Object-Oriented Programming (OOP) concepts.
It is a command-line based application that allows management of books, members, and borrowing/returning of books.
The project demonstrates the use of classes, objects, methods, encapsulation, and basic CLI interaction.

🎯 Project Objective
To build a simple system that:
Manages library books
Manages library members
Allows members to borrow and return books
Uses Python OOP principles effectively

🧠 Concepts Used
Classes and Objects
Methods and Attributes
Lists to store objects
Conditional logic
Command Line Interface (CLI)

🧩 Classes Implemented
1️⃣ Book Class
Attributes:
book_id
title
author
status (Available / Borrowed)
Methods:
__init__()
__str__()
borrow_book()
return_book()

2️⃣ Member Class
Attributes:
member_id
name
borrowed_books (list)
Methods:
__init__()
__str__()
borrow_book(book)
return_book(book)

3️⃣ Library Class
Attributes:
books (list of Book objects)
members (list of Member objects)
Methods:
add_book()
add_member()
search_book()
search_member()
display_books()
display_members()
borrow_book()
return_book()

🖥️ Features
✔ Add books to the library
✔ Add members to the library
✔ Display all books and members
✔ Search for books and members
✔ Borrow books
✔ Return books
✔ Simple menu-driven CLI

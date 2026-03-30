Library Management System

This project is a simple command-line application built using Python to demonstrate Object-Oriented Programming (OOP) concepts.

Overview

The system simulates a basic library where users can:

Register in the system
View available books
Borrow books
Return books

It is designed to showcase clean code structure and fundamental OOP principles.

Concepts Used
Classes and objects
Encapsulation
Separation of responsibilities
Basic data handling
Method interaction between objects
Project Structure
library_system/
├── main.py        # Entry point of the application
├── models.py      # Core classes (Library, Book, User)
├── data.py        # Sample data for books and users
├── README.md      # Project documentation
How to Run

Navigate to the project folder:

cd oop/library_system

Run the program:

python main.py
Example Features
Borrowing a book updates its availability
Users can only return books they have borrowed
The system validates user and book existence
Possible Improvements
Add persistent storage (JSON or database)
Implement user roles (e.g., Admin, Member)
Add search functionality
Build a graphical or web interface
Purpose

This project is part of my Python portfolio and reflects my progress in learning how to design and structure applications using OOP.
#Library Management System

A robust, Command-Line Interface (CLI) based Library Management System built with Python and SQLite3. This application allows librarians to efficiently manage book inventories, organize bookshelves, track library members, and handle the issuing and returning of books (including automated fine calculations).

---

## Features

The system is divided into three main operational modules:

### 1. Library Settings (Inventory Management)
* **Dynamic Bookshelves:** Create and delete specific bookshelves (e.g., `bookshelf1`, `bookshelf2`) to organize inventory.
* **Book Management:** Add, remove, update, and display books.
* **Search Capabilities:** Find books easily by Book ID, Name, or Author.
* **Relocation:** Move books from one bookshelf to another.

### 2. Customer Settings (User Management)
* **Member Registration:** Add new customers and auto-generate unique User IDs (UID).
* **Database Management:** Update, delete, and display all registered customers.
* **Search:** Locate member profiles using their UID or Name.

### 3. Book Settings (Transactions)
* **Issue Books:** Check out books to registered users. Automatically updates stock quantity and generates a receipt.
* **Return Books:** Process book returns using the receipt number. Automatically calculates late fines (₹10 per day after 14 days) and restores stock quantity.
* **Tracking:** View currently borrowed books and complete transaction history.
* **Advanced Transaction Search:** Search borrowed lists and history by UID, Name, Book ID, or Date.

---

## Prerequisites

This script uses only built-in Python libraries. No external packages or `pip` installations are required.
* Python 3.x
* Built-in modules used: `sqlite3`, `math`, `datetime`

---

## Installation & Setup

1.  Clone or download the script to your local machine.
2.  Save the file as `library_management.py` (or your preferred name).
3.  Open your terminal or command prompt.
4.  Navigate to the directory where the file is saved.
5.  Run the script using Python:

```bash
python library_management.py

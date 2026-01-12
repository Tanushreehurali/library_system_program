# Test file for library management system

from library import add_book, issue_book, return_book

def test_add_book():
    book = add_book(1, "Python", "gudio", 3)
    assert book["qty"] == 3

def test_issue_book():
    book = add_book(2, "DBMS", "Korth", 1)
    result = issue_book(book)
    assert result == "Book Issued"

def test_issue_not_available():
    book = add_book(3, "OS", "Galvin", 0)
    result = issue_book(book)
    assert result == "Book Not Available"

def test_return_book():
    book = add_book(4, "CN", "Tanenbaum", 1)
    result = return_book(book)
    assert result == "Book Returned"

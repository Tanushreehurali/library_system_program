# Program to manage library books

def add_book(book_id, title, author, qty):
    return {
        "id": book_id,
        "title": title,
        "author": author,
        "qty": qty
    }

def issue_book(book):
    if book["qty"] > 0:
        book["qty"] -= 1
        return "Book Issued"
    else:
        return "Book Not Available"

def return_book(book):
    book["qty"] += 1
    return "Book Returned"

def display_book(book):
    print("\n=== Book Details ===")
    print(f"Book ID    : {book['id']}")
    print(f"Title      : {book['title']}")
    print(f"Author     : {book['author']}")
    print(f"Quantity   : {book['qty']}")


if __name__ == "__main__":
    import sys
    print("=== Library Management System ===")

    # Get inputs from command line (Jenkins parameters)
    if len(sys.argv) == 5:
        book_id = int(sys.argv[1])
        title   = sys.argv[2]
        author  = sys.argv[3]
        qty     = int(sys.argv[4])
    else:
        # Defaults for manual run
        book_id = 1
        title   = "Python"
        author  = "Guido"
        qty     = 3

    # Add book
    book = add_book(book_id, title, author, qty)
    display_book(book)

    # Issue & Return
    print("\nOperation Results")
    print(issue_book(book))
    print(return_book(book))

    display_book(book)  # Final state
valid input. Please enter valid values.")

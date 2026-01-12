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


if __name__ == "__main__":
    import sys
    print("=== Library Management System ===")

    try:
        # If user gives input through command line
        # python library.py 1 Python Guido 3
        if len(sys.argv) == 5:
            book_id = int(sys.argv[1])
            title = sys.argv[2]
            author = sys.argv[3]
            qty = int(sys.argv[4])

        else:
            # Take user input
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            qty = int(input("Enter Quantity: "))

        print("\n=== Book Details ===")
        print(f"Book ID    : {book_id}")
        print(f"Title      : {title}")
        print(f"Author     : {author}")
        print(f"Quantity   : {qty}")

        book = add_book(book_id, title, author, qty)

        print("\nOperation Results")
        print(issue_book(book))
        print(return_book(book))

        print("\nFinal Book Data:", book)

    except ValueError:
        print("Invalid input. Please enter valid values.")

library = []


def add_book():
    book = input("Enter book name: ")
    library.append(book)
    print("Book added")


def issue_book():
    book = input("Enter book name to issue: ")
    if book in library:
        library.remove(book)
        print("Book issued")
    else:
        print("Book not available")


def return_book():
    book = input("Enter book name to return: ")
    library.append(book)
    print("Book returned")


def search_book():
    book = input("Enter book name to search: ")
    if book in library:
        print("Book is available")
    else:
        print("Book not found")


add_book()
add_book()
search_book()
issue_book()
return_book()
search_book()

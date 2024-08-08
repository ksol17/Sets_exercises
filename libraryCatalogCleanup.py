def remove_book(catalog):
    book_title = input("Enter the book title to remove: ")
    if book_title in catalog:
        catalog.remove(book_title)
        print(f"{book_title} has been removed from the catalog.")
    else:
        print(f"{book_title} not found in the catalog.")


def display_catalog(catalog):
    print("Current catalog:")
    for book in catalog:
        print(f"- {book}")

catalog = {"To Kill a Mockingbird", "1984", "The Great Gatsby", "Pride and Prejudice"}
while True:
    print("\n1. Remove a book")
    print("2. Display catalog")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        remove_book(catalog)
    elif choice == '2':
        display_catalog(catalog)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
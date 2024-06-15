import json
BOOKS_FILE = "books.txt"

def main():
    books = load_books()

    while True:
        print("Book Registration")
        print("1. Add a book")
        print("2. View all books")
        print("3. Find a book by title")
        print("4. Find a book by Author")
        print("5. Delete a book by index")
        print("6. Exit")

        choice = input("Enter your choice: ")
        print()

        if choice == '1':
            add_book(books)
        elif choice == '2':
            view_books(books)
        elif choice == '3':
            find_book_by_title(books)
        elif choice == '4':
            find_book_by_author(books)
        elif choice == '5':
            delete_book_by_index(books)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

def load_books():
    try:
        with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
            books = json.load(file)
            print(f"Loaded {len(books)} book(s) from the file.\n")
            return books
    except FileNotFoundError:
        print("No existing books file found. Starting with an empty list.\n")
        return[]
    except json.JSONDecodeError:
        print("Error reading the books file. Starting with an empty list.\n")
        return[]

def save_books(books):
    try:
        with open(BOOKS_FILE, 'w', encoding='utf-8') as file:
            json.dump(books, file, ensure_ascii=False, indent=4)
        print("Books have been saved to the file.\n")
    except IOError as e:
        print(f"An error occurred while saving the books: {e}")


def add_book(books):
    title = input("Enter the book title: ")
    # Check for duplicate titles
    duplicate_books = [book for book in books if book['Title'].strip().lower() == title.strip().lower()]
    if duplicate_books:
        print(f"There are already {len(duplicate_books)} book(s) with the title '{title}':")
        for i, book in enumerate(duplicate_books, 1):
            print(f"Book {i}:")
            print(f"Title: {book['Title']}")
            print(f"Author: {book['Author']}")
            print(f"Year: {book['Year']}")
            print(f"ISBN: {book['ISBN']}")
            print(f"Bookcase: {book['Bookcase']}")
            print(f"Shelf: {book['Shelf']}")
            print()
        
        choice = input("Do you still want to add the book? (y/n): ").strip().lower()
        if choice != 'y':
            print("Book not added.\n")
            return

    author = input("Enter the book author: ")
    year = input("Enter the year of publication: ")
    isbn = input("Enter the ISBN: ")
    bookcase = input("Enter the bookcase: ")
    shelf = input("Enter the shelf: ")
    if not (title and author and year and isbn and bookcase and shelf):
        print("Error: All fields must be filled out.")
        return
    
    # Create a book dictionary and add it to the list
    book = {"Title": title,
            "Author": author,
            "Year": year,
            "ISBN": isbn,
            "Bookcase": bookcase,
            "Shelf": shelf
            }
    books.append(book)
    save_books(books)
    print("Book added successfully.\n")

def view_books(books):
    if not books:
        print("No books registered.\n")
        return
    print("Registered Books:")
    for i, book in enumerate(books, 1):
        print(f"Book {i}:")
        print(f"Title: {book['Title']}")
        print(f"Author: {book['Author']}")
        print(f"Year: {book['Year']}")
        print(f"ISBN: {book['ISBN']}")
        print(f"Bookcase: {book['Bookcase']}")
        print(f"Shelf: {book['Shelf']}")
        print()


def find_book_by_title(books):
    title_to_find = input("Enter the title of the book to find: ").strip().lower()
    search_words = title_to_find.split()
    
    found_books = [book for book in books
                  if any(word in book['Title'].strip().lower() for word in search_words)]
    
    if not found_books:
        print("No books found with that title.\n")
        return
    
    print(f"Found {len(found_books)} book(s) with the title '{title_to_find}':")
    for i, book in enumerate(found_books, 1):
        print(f"Book {i}:")
        print(f"Title: {book['Title']}")
        print(f"Author: {book['Author']}")
        print(f"Year: {book['Year']}")
        print(f"ISBN: {book['ISBN']}")
        print(f"Bookcase: {book['Bookcase']}")
        print(f"Shelf: {book['Shelf']}")
        print()

    
    #print("No books found with that title.\n")        


def find_book_by_author(books):
    author_to_find = input("Enter the author of the book to find: ").strip().lower()
    search_words = author_to_find.split()
    
    found_books = [book for book in books
                  if any(word in book['Author'].strip().lower() for word in search_words)]
    
    if not found_books:
        print("No books found with that author.\n")
        return
    
    print(f"Found {len(found_books)} book(s) with the author '{author_to_find}':")
    for i, book in enumerate(found_books, 1):
        print(f"Book {i}:")
        print(f"Title: {book['Title']}")
        print(f"Author: {book['Author']}")
        print(f"Year: {book['Year']}")
        print(f"ISBN: {book['ISBN']}")
        print(f"Bookcase: {book['Bookcase']}")
        print(f"Shelf: {book['Shelf']}")
        print()

    
    #print("No books found with that author.\n")   

def delete_book_by_index(books):
    if not books:
        print("No books registered.\n")
        return
    try:
        index_to_delete = int(input("Enter the index of the book to delete: "))-1
        if index_to_delete < 0 or index_to_delete >= len(books):
            print("Invalid index.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    # Confirm deletion
    confirm = input(f"Are you sure you want to delete the book '{books[index_to_delete]['Title']}? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Book deletion cancelled.\n")
        return
    
    # Delete the selected book
    del books[index_to_delete]
    save_books(books)
    print("Book deleted successfully.\n")


if __name__ == "__main__":
    main()
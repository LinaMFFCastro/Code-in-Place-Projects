import json
import tkinter as tk
from tkinter import messagebox, simpledialog

BOOKS_FILE = "books.json"

def load_books():
    try:
        with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
            books = json.load(file)
            return books
    except (FileNotFoundError, json.JSONDecodeError):
        return[]


def save_books(books):
    try:
        with open(BOOKS_FILE, 'w', encoding='utf-8') as file:
            json.dump(books, file, ensure_ascii=False, indent=4)
    except IOError as e:
        messagebox.showerror("Error", f"An error occurred while saving the books: {e}")



class BookManager:
    def __init__(self, root):
        self.books = load_books()
        self.root = root
        self.root.title("Book Registration")

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        tk.Label(frame, text="Title").grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(frame, width=50)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Author").grid(row=1, column=0, padx=5, pady=5)
        self.author_entry = tk.Entry(frame, width=50)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Year").grid(row=2, column=0, padx=5, pady=5)
        self.year_entry = tk.Entry(frame, width=50)
        self.year_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="ISBN").grid(row=3, column=0, padx=5, pady=5)
        self.isbn_entry = tk.Entry(frame, width=50)
        self.isbn_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame, text="Bookcase").grid(row=4, column=0, padx=5, pady=5)
        self.bookcase_entry = tk.Entry(frame, width=50)
        self.bookcase_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(frame, text="Shelf").grid(row=5, column=0, padx=5, pady=5)
        self.shelf_entry = tk.Entry(frame, width=50)
        self.shelf_entry.grid(row=5, column=1, padx=5, pady=5)

        self.add_button = tk.Button(frame, text="Add book", command=self.add_book)
        self.add_button.grid(row=7, column=0, padx=5, pady=5)

        self.view_button = tk.Button(frame, text="View all book", command=self.view_books)
        self.view_button.grid(row=7, column=1, padx=5, pady=5)

        self.find_title_button = tk.Button(frame, text="Find books by Title", command=self.find_book_by_title)
        self.find_title_button.grid(row=8, column=0, padx=5, pady=5)

        self.find_author_button = tk.Button(frame, text="Find books by Author", command=self.find_book_by_author)
        self.find_author_button.grid(row=8, column=1, padx=5, pady=5)

        self.update_button = tk.Button(frame, text="Update book by index", command=self.update_book_by_index)
        self.update_button.grid(row=9, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(frame, text="Delete book by index", command=self.delete_book_by_index)
        self.delete_button.grid(row=9, column=1, padx=5, pady=5)

        self.exit_button = tk.Button(frame, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=10, column=0, padx=5, pady=5)

    def add_book(self):
        title = self.title_entry.get().strip()

        # Check for duplicate titles
        duplicate_books = [book for book in self.books if book['Title'].strip().lower() == title.strip().lower()]
        if duplicate_books:
            msg = f"There are already {len(duplicate_books)} book(s) with the title '{title}':\n"
            for book in duplicate_books:
                msg += f"Title: {book['Title']}\n Author: {book['Author']}\n Year: {book['Year']}\n ISBN: {book['ISBN']}\n Bookcase: {book['Bookcase']}\n Shelf: {book['Shelf']}\n\n"
            
            msg += "Do you still want to add the book?"
            if not messagebox.askyesno("Duplicate Title", msg):
                return

        author = self.author_entry.get().strip()
        year = self.year_entry.get().strip()
        isbn = self.isbn_entry.get().strip()
        bookcase = self.bookcase_entry.get().strip()
        shelf = self.shelf_entry.get().strip()
        if not (title and author and year and isbn and bookcase and shelf):
            messagebox.showerror("Error", "All fields must be filled out.")
            return
        
        # Create a book dictionary and add it to the list
        book = {"Title": title,
                "Author": author,
                "Year": year,
                "ISBN": isbn,
                "Bookcase": bookcase,
                "Shelf": shelf
                }
        
        self.books.append(book)
        save_books(self.books)
        messagebox.showinfo("Success", "Book added successfully.")
        self.clear_entries()
    
   
    
    
    def view_books(self):
        if not self.books:
            messagebox.showinfo("Information", "No books registered.")
            return
        
        books_str = "Registered Books:\n\n"
        for i, book in enumerate(self.books, 1):
            books_str += f"Book {i}:\n Title: {book['Title']}\n Author: {book['Author']}\n Year: {book['Year']}\n ISBN: {book['ISBN']}\n Bookcase: {book['Bookcase']}\n Shelf: {book['Shelf']}\n\n"
        
        self.show_text_in_popup("View all Books", books_str)

    def find_book_by_title(self):
        title_to_find = simpledialog.askstring("Find Books by Title", "Enter the words to search in the book title:").strip().lower()
        if not title_to_find:
            return
        
        search_words = title_to_find.split()
        found_books = [
            book for book in self.books 
            if any(word in book['Title'].strip().lower() for word in search_words)
        ]

        if not found_books:
            messagebox.showinfo("Information", "No books found with the given words in their title.")
            return
        
        books_str = f"Found {len(found_books)} book(s) with the given words in their title:\n\n"
        for i, book in enumerate(found_books, 1):
            books_str += f"Book {i}:\n  Title: {book['Title']}\n  Author: {book['Author']}\n  Year: {book['Year']}\n  ISBN: {book['ISBN']}\n Bookcase: {book['Bookcase']}\n Shelf: {book['Shelf']}\n\n"
        
        self.show_text_in_popup("Found Books", books_str)      


    def find_book_by_author(self):
        author_to_find = simpledialog.askstring("Find Books by Author", "Enter the words to search in the book author:").strip().lower()
        if not author_to_find:
            return
        
        search_words = author_to_find.split()
        found_books = [
            book for book in self.books 
            if any(word in book['Author'].strip().lower() for word in search_words)
        ]

        if not found_books:
            messagebox.showinfo("Information", "No books found with the given words in their author.")
            return
        
        books_str = f"Found {len(found_books)} book(s) with the given words in their author:\n\n"
        for i, book in enumerate(found_books, 1):
            books_str += f"Book {i}:\n  Title: {book['Title']}\n  Author: {book['Author']}\n  Year: {book['Year']}\n  ISBN: {book['ISBN']}\n Bookcase: {book['Bookcase']}\n Shelf: {book['Shelf']}\n\n"
        
        self.show_text_in_popup("Found Books", books_str) 


    def update_book_by_index(self):
        if not self.books:
            messagebox.showinfo("Information", "No books registered.")
            return
        
        self.view_books()

        try:
            index_to_update = int(simpledialog.askstring("Update Book by Index", "Enter the number of the book to update: "))-1
            if index_to_update < 0 or index_to_update >= len(self.books):
                messagebox.showerror("Error", "Invalid number.")
                return
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
            return
        
        book = self.books[index_to_update]

        title = simpledialog.askstring("Update Book", f"Enter the new book title (or press enter to keep '{book['Title']}'): ")
        author = simpledialog.askstring("Update Book", f"Enter the new book author (or press enter to keep '{book['Author']}'): ")
        year = simpledialog.askstring("Update Book", f"Enter the new book year (or press enter to keep '{book['Year']}'): ")
        isbn = simpledialog.askstring("Update Book", f"Enter the new book ISBN (or press enter to keep '{book['ISBN']}'): ")
        bookcase = simpledialog.askstring("Update Book", f"Enter the new bookcase (or press enter to keep '{book['Bookcase']}'): ")
        shelf = simpledialog.askstring("Update Book", f"Enter the new book shelf (or press enter to keep '{book['Shelf']}'): ")
        
        # Update the selected book
        if title:
            book['Title'] = title
        if author:
            book['Author'] = author
        if year:
            book['Year'] = year
        if isbn:
            book['ISBN'] = isbn
        if bookcase:
            book['Bookcase'] = bookcase
        if shelf:
            book['Shelf'] = shelf
        
        save_books(self.books)
        messagebox.showinfo("Success", "Book updated successfully.")


    
    def delete_book_by_index(self):
        if not self.books:
            messagebox.showinfo("Information", "No books registered.")
            return
        
        self.view_books()

        try:
            index_to_delete = int(simpledialog.askstring("Delete Book by Index", "Enter the number of the book to delete: "))-1
            if index_to_delete < 0 or index_to_delete >= len(self.books):
                messagebox.showerror("Error", "Invalid number.")
                return
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
            return
        
        # Confirm deletion
        book_title = self.books[index_to_delete]['Title']
        if not messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the book '{book_title}'?"):
            print("Book deletion cancelled.\n")
            return
        
        # Delete the selected book
        del self.books[index_to_delete]
        save_books(self.books)
        messagebox.showinfo("Success", "Book deleted successfully.")
        
    
    
    def show_text_in_popup(self, title, text):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("400x300")
        text_widget = tk.Text(popup, wrap="word", padx=10, pady=10)
        text_widget.insert("1.0", text)
        text_widget.config(state="disable")
        text_widget.pack(expand=True, fill="both")
        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)
        self.bookcase_entry.delete(0, tk.END)
        self.shelf_entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = BookManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
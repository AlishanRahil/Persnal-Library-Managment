import json
import os

# File to store book data
LIBRARY_FILE = "library.json"

# Load library from file (if exists)
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)


 #  Making the add book function 

def add_book(library):
    title = input("Enter The Book Title")
    author = input("Enter The Author")
    year = input("Enter The Publication Year")
    genre = input("Enter The Book Genre")
    read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"


    book = {
        "title":title,
        "author":author,
        "year":year,
        "genre":genre,
        "read":read
    }


    library.append(book)
    save_library(library)
    print(f"\n✅ '{title}' added successfully!\n")


#     for removing the book i m making another function 

def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print(f"\n❌ '{title}' removed successfully!\n")
            return
    print("\n⚠ Book not found!\n")


#  Making another for search books 

def search_book(library):
    title = input("Enter the title to search for: ")
    for book in library:
        if book["title"].lower() == title.lower():
            print("\n📖 Book Found:")
            print_book(book)
            return
    print("\n⚠ Book not found!\n")


def list_books(library):
    if not library:
        print("\n📚 Your library is empty!\n")
        return
    print("\n📚 Your Book Collection:")
    for idx, book in enumerate(library, start=1):
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Not Read'}")
    print()


def update_read_status(library):
    title = input("Enter the title of the book: ")
    for book in library:
        if book["title"].lower() == title.lower():
            book["read"] = not book["read"]
            save_library(library)
            status = "Read" if book["read"] else "Not Read"
            print(f"\n✅ '{title}' marked as {status}\n")
            return
    print("\n⚠ Book not found!\n")

# Show statistics
def show_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    unread_books = total_books - read_books

    print("\n📊 Library Statistics:")
    print(f"📚 Total Books: {total_books}")
    print(f"✅ Books Read: {read_books}")
    print(f"❌ Books Unread: {unread_books}\n")

# Display book details
def print_book(book):
    print(f"\n📖 Title: {book['title']}")
    print(f"✍ Author: {book['author']}")
    print(f"📅 Year: {book['year']}")
    print(f"📂 Genre: {book['genre']}")
    print(f"📖 Read: {'✅ Yes' if book['read'] else '❌ No'}\n")

# Main menu
def main():
    library = load_library()

    while True:
        print("\n📚 Personal Library Manager")
        print("1️⃣ Add a Book")
        print("2️⃣ Remove a Book")
        print("3️⃣ Search for a Book")
        print("4️⃣ List All Books")
        print("5️⃣ Mark Book as Read/Unread")
        print("6️⃣ Show Statistics")
        print("7️⃣ Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            list_books(library)
        elif choice == "5":
            update_read_status(library)
        elif choice == "6":
            show_statistics(library)
        elif choice == "7":
            print("\n👋 Goodbye! Happy Reading!\n")
            break
        else:
            print("\n⚠ Invalid choice! Please enter a number from 1 to 7.\n")

if __name__ == "__main__":
    main()


import json
import os
import streamlit as st

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

# Display book details
def print_book(book):
    st.write(f"**Title:** {book['title']}")
    st.write(f"**Author:** {book['author']}")
    st.write(f"**Year:** {book['year']}")
    st.write(f"**Genre:** {book['genre']}")
    st.write(f"**Read:** {'✅ Yes' if book['read'] else '❌ No'}")
    st.markdown("---")

# Streamlit App
def main():
    st.set_page_config(page_title="Personal Library Manager", page_icon="📚")
    st.title("📚 Personal Library Manager")

    # Initialize session state
    if "library" not in st.session_state:
        st.session_state.library = load_library()

    menu = ["Add a Book", "Remove a Book", "Search for a Book", "List All Books",
            "Mark Book as Read/Unread", "Show Statistics"]
    choice = st.sidebar.selectbox("Select Action", menu)

    if choice == "Add a Book":
        st.header("➕ Add a New Book")
        title = st.text_input("Enter Book Title")
        author = st.text_input("Enter Author")
        year = st.text_input("Enter Publication Year")
        genre = st.text_input("Enter Book Genre")
        read = st.checkbox("Have you read this book?")

        if st.button("Add Book"):
            new_book = {
                "title": title,
                "author": author,
                "year": year,
                "genre": genre,
                "read": read
            }
            st.session_state.library.append(new_book)
            save_library(st.session_state.library)
            st.success(f"✅ '{title}' added successfully!")

    elif choice == "Remove a Book":
        st.header("❌ Remove a Book")
        titles = [book['title'] for book in st.session_state.library]
        if titles:
            selected_title = st.selectbox("Select Book to Remove", titles)
            if st.button("Remove Book"):
                st.session_state.library = [book for book in st.session_state.library if book['title'] != selected_title]
                save_library(st.session_state.library)
                st.success(f"❌ '{selected_title}' removed successfully!")
        else:
            st.info("Your library is empty.")

    elif choice == "Search for a Book":
        st.header("🔍 Search for a Book")
        search_title = st.text_input("Enter the title to search for")
        if st.button("Search"):
            found = False
            for book in st.session_state.library:
                if book["title"].lower() == search_title.lower():
                    st.success("Book Found!")
                    print_book(book)
                    found = True
                    break
            if not found:
                st.warning("⚠ Book not found!")

    elif choice == "List All Books":
        st.header("📚 Your Book Collection")
        if not st.session_state.library:
            st.info("Your library is empty!")
        else:
            for idx, book in enumerate(st.session_state.library, start=1):
                st.subheader(f"{idx}. {book['title']} by {book['author']}")
                print_book(book)

    elif choice == "Mark Book as Read/Unread":
        st.header("✅/❌ Toggle Read Status")
        titles = [book['title'] for book in st.session_state.library]
        if titles:
            selected_title = st.selectbox("Select Book", titles)
            if st.button("Toggle Read/Unread"):
                for book in st.session_state.library:
                    if book["title"] == selected_title:
                        book["read"] = not book["read"]
                        save_library(st.session_state.library)
                        status = "Read" if book["read"] else "Not Read"
                        st.success(f"✅ '{selected_title}' marked as {status}")
                        break
        else:
            st.info("Your library is empty!")

    elif choice == "Show Statistics":
        st.header("📊 Library Statistics")
        total_books = len(st.session_state.library)
        read_books = sum(1 for book in st.session_state.library if book["read"])
        unread_books = total_books - read_books

        st.write(f"📚 Total Books: {total_books}")
        st.write(f"✅ Books Read: {read_books}")
        st.write(f"❌ Books Unread: {unread_books}")

if __name__ == "__main__":
    main()

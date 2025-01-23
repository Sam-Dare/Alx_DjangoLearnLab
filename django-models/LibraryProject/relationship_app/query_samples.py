from relationship_app.models import Author, Book, Library, Librarian

# Query to fetch an author by name
def fetch_author_by_name(author_name):
    author = Author.objects.get(name=author_name)  # Ensure this is present
    return author

# Query to get all books by a specific author
def fetch_books_by_author(author_name):
    author = fetch_author_by_name(author_name)  # Call the function defined above
    books = Book.objects.filter(author=author)  # Ensure this is present
    return books

# Query to list all books in a library
def fetch_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Query to retrieve the librarian for a library
def fetch_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

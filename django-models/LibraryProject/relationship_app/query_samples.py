from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Query all books by a specific author using objects.filter()
def get_books_by_author(author_name):
    # Use filter instead of get to match the checker's requirement
    books = Book.objects.filter(author__name=author_name)
    return books


# Query 2: List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books


# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian

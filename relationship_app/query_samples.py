from relationship_app.models import Author, Library
def get_books_by_author(author_name):
    """
    Return a QuerySet of books written by the author with the given name.
    Example: get_books_by_author("J.K. Rowling")
    """
    return Author.objects.get(name=author_name).book_set.all()
def get_books_in_library(library_name):
    """
    Return a QuerySet of books in the library with the given name.
    Example: get_books_in_library("Central Library")
    """
    return Library.objects.get(name=library_name).books.all()

def get_librarian_for_library(library_name):
    """
    Return the Librarian instance for the given library name.
    Example: get_librarian_for_library("Central Library")
    """
    return Library.objects.get(name=library_name).librarian

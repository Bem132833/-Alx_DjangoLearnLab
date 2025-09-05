from relationship_app.models import Author, Library
author = Author.objects.get(name="Author Name")
books_by_author = author.book_set.all()
library = Library.objects.get(name="Library Name")
books_in_library = library.books.all()
librarian = library.librarian

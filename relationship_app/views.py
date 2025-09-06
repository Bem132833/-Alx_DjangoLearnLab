from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    """
    Function-based view that returns a plain-text list of book titles and authors.
    """
    books = Book.objects.select_related('author').all()
    lines = [f"{b.title} by {b.author.name}" for b in books]
    return HttpResponse("\n".join(lines), content_type="text/plain")

class LibraryDetailView(DetailView):
    """
    Class-based DetailView for Library that provides 'library' in context.
    Template: relationship_app/library_detail.html
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

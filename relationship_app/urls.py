from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view: list all books (plain-text output)
    path('books/', views.list_books, name='list_books'),

    # Class-based view: library detail (pk = library id)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

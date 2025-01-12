from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # FBV for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # CBV for library details
]
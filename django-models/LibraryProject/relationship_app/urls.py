from django.urls import path
from .views import (
    add_book,
    edit_book,
    delete_book,
    list_books,
    LibraryDetailView,
    register,
    user_login,
    user_logout,
    admin_view,
    librarian_view,
    member_view
)

urlpatterns = [
    # Book and Library URLs
     path('books/add/', add_book, name='add_book'),  # URL for adding books
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),  # URL for editing books
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),  # URL for deleting books
    path('books/', list_books, name='list_books'),  # FBV for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # CBV for library details

    # User Authentication URLs
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    # Role-Based Access URLs
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]

from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView  # Importing LoginView and LogoutView

urlpatterns = [
    # Book and Library URLs
    path('books/add_book/', views.add_book, name='add_book'),  # URL for adding books
    path('books/<int:pk>/edit_book/', views.edit_book, name='edit_book'),  # URL for editing books
    path('books/<int:pk>/delete_book/', views.delete_book, name='delete_book'),  # URL for deleting books
    path('books/', list_books, name='list_books'),  # FBV for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # CBV for library details

    # User Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # CBV for login
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # CBV for logout

    # Role-Based Access URLs
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]

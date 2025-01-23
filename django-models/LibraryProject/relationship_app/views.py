from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.detail import DetailView
from relationship_app.models import Book, Library, UserProfile
from relationship_app.forms import BookForm  # Assuming you have a form for handling Book objects


# Function-based view to list all books
@login_required  # Restrict access to authenticated users
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Function-based view to add a book (restricted to librarians or admins)
@user_passes_test(lambda u: is_librarian(u) or is_admin(u))
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Redirect to the list_books view
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})


# Function-based view to edit a book
@user_passes_test(lambda u: is_librarian(u) or is_admin(u))
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Redirect to the list_books view
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})


# Function-based view to delete a book
@user_passes_test(lambda u: is_librarian(u) or is_admin(u))
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})


# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, role='Member')  # Assign default role as 'Member'
            login(request, user)  # Automatically log the user in after registration
            return redirect('list_books')  # Redirect to the list_books view
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')  # Redirect to the list_books view
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# User Logout View
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')


# Role-Based Views

# Check if the user is an admin
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'


# Check if the user is a librarian
def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'


# Check if the user is a member
def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'


# Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# Member View
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

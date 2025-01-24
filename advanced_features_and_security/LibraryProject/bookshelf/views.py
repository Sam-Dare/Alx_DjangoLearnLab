from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Book
from .forms import ExampleForm


def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # You can save this data or send an email, etc.
            return render(request, 'bookshelf/form_success.html', {'name': name})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})


@permission_required('your_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'your_app/book_list.html', {'books': books})

@permission_required('your_app.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect('book_list')
    return render(request, 'your_app/book_form.html')

@permission_required('your_app.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('book_list')
    return render(request, 'your_app/book_form.html', {'book': book})

@permission_required('your_app.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

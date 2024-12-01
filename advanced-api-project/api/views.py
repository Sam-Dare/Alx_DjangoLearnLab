# from django.shortcuts import render
# from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, serializers, permissions, filters
from django_filters import rest_framework

from .models import Book
from .serializers import BookSerializer

# ListView - Retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']  # Fields to order by
    ordering = ['title']  # Default ordering

# DetailView - Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# CreateView - Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only

    def perform_create(self, serializer):
        # Custom validation logic
        if serializer.validated_data['publication_year'] > 2024:  # Example check
            raise serializers.ValidationError("Publication year cannot be in the future.")
        serializer.save()

        # UpdateView - Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only

    def get_object(self):
        # Assuming book ID is passed in the request body (or you can change it to another method)
        book_id = self.request.data.get('id')
        return Book.objects.get(pk=book_id)

# DeleteView - Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only

    def get_object(self):
        # Assuming book ID is passed in the request body (or you can change it to another method)
        book_id = self.request.data.get('id')
        return Book.objects.get(pk=book_id)


# # UpdateView - Modify an existing book
# class BookUpdateView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Authenticated users only

# # DeleteView - Remove a book
# class BookDeleteView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Authenticated users only

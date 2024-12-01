from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# ListAPIView for listing all books
class BookList(ListAPIView):
    """
    A view for listing all books in the database.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ModelViewSet for handling CRUD operations
class BookViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Require authentication for all operations

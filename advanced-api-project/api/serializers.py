from rest_framework import serializers
from .models import Author, Book
import datetime

# Serializers for the API
# BookSerializer: Serializes Book instances, including validation for publication_year.
# AuthorSerializer: Serializes Author instances, including nested BookSerializer for related books.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

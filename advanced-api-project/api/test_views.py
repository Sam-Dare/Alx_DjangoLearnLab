from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        """
        Set up test environment.
        """
        # Create a user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create sample books
        self.book1 = Book.objects.create(title="Book One", author=self.author1, publication_year=2023)
        self.book2 = Book.objects.create(title="Book Two", author=self.author2, publication_year=2024)

        # Define URLs
        self.book_list_url = reverse("book-list")
        self.book_detail_url = reverse("book-detail", args=[self.book1.id])
        self.book_create_url = reverse("book-create")

    def test_list_books(self):
        """
        Ensure the book list endpoint returns the correct data.
        """
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Check that two books are returned

    def test_create_book(self):
        """
        Test book creation.
        """
        data = {"title": "Book Three", "author": self.author1.id, "publication_year": 2022}
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # Ensure a book was added

    def test_update_book(self):
        """
        Test updating a book.
        """
        data = {"title": "Updated Book One", "author": self.author1.id, "publication_year": 2023}
        response = self.client.put(self.book_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")



    def test_delete_book(self):
        """
        Test deleting a book.
        """
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Ensure a book was deleted

    def test_search_books(self):
        """
        Ensure searching works on the book list endpoint.
        """
        response = self.client.get(f"{self.book_list_url}?search=Book One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only "Book One" should match

    def test_filter_books(self):
        """
        Ensure filtering works on the book list endpoint.
        """
        response = self.client.get(f"{self.book_list_url}?author={self.author1.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only books by "Author One" should match

    def test_order_books(self):
        """
        Ensure ordering works on the book list endpoint.
        """
        response = self.client.get(f"{self.book_list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if books are returned in ascending order of publication_year
        self.assertTrue(response.data[0]['publication_year'] <= response.data[1]['publication_year'])

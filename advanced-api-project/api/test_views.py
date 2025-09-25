from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()

        # Create an author
        self.author = Author.objects.create(name="J.K. Rowling")

        # Create some books
        self.book1 = Book.objects.create(title="Harry Potter 1", publication_year=2001, author=self.author)
        self.book2 = Book.objects.create(title="Harry Potter 2", publication_year=2003, author=self.author)

        # Endpoints
        self.list_url = reverse("book-list")   # /books/
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book1.pk})  # /books/<id>/

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book_requires_authentication(self):
        data = {"title": "New Book", "publication_year": 2025, "author": self.author.id}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        data = {"title": "New Book", "publication_year": 2020, "author": self.author.id}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        data = {"title": "Updated Title", "publication_year": 2001, "author": self.author.id}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_publication_year(self):
        response = self.client.get(self.list_url, {"publication_year": 2001})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {"search": "Harry Potter 2"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_year(self):
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data[0]["publication_year"], response.data[1]["publication_year"])


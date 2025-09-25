from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed, created, updated, or deleted.
    Includes filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["title", "author", "publication_year"]

    # Fix search: handle title, author name (FK), and year
    search_fields = ["title", "author__name", "publication_year"]

    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]


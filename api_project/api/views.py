from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer


# Old ListAPIView (read-only endpoint)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# New ViewSet (full CRUD)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


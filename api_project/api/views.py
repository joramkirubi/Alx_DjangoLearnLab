from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer


# Old ListAPIView (read-only endpoint)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # 👈 Only logged-in users can list books


# New ViewSet (full CRUD)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]  # 👈 Only admins can CRUD


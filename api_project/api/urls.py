from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet  # 👈 import BookViewSet

# Create router and register BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Simple ListAPIView endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # Router endpoints (CRUD for Book model)
    path('', include(router.urls)),
]


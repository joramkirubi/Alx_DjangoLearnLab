from django.urls import path
from .views import ListCreateView, DetailView, UpdateView, DeleteView, BookListView

urlpatterns = [
    path("books/", ListCreateView.as_view(), name="list_create_books"),
    path("books/<int:pk>/", DetailView.as_view(), name="book_detail"),
    path("books/<int:pk>/update/", UpdateView.as_view(), name="book_update"),
    path("books/<int:pk>/delete/", DeleteView.as_view(), name="book_delete"),
    path("books/list/", BookListView.as_view(), name="book_list_view"),  # ✅ new one
]


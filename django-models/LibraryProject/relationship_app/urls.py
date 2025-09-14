from django.urls import path
from .views import list_books, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("books/", list_books, name="list_books"),  # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # class-based view
    path("register/", register, name="register"),  # registration
    path("login/", LoginView.as_view(), name="login"),  # login view
    path("logout/", LogoutView.as_view(), name="logout"),  # logout view
]


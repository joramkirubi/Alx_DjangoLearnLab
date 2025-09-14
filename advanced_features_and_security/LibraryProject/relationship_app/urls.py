from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    path("register/", views.register, name="register"),
    path("login/", views.LoginView, name="login"),   # use the alias from views.py
    path("logout/", views.LogoutView, name="logout"),  # same here

    # role-based views
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
]


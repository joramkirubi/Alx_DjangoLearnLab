from django.urls import path
from . import views   
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("books/", list_books, name="list_books"),  # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # class-based view
    path("register/", views.register, name="register"),  # registration
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),  # login view
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),  # logout view

     # role-based views
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
]


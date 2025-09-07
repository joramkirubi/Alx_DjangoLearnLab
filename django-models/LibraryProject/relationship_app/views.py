from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view: plain text list of "title by author"
def list_books(request):
    books = Book.objects.select_related('author').all()
    lines = [f"{b.title} by {b.author.name}" for b in books]
    return HttpResponse("\n".join(lines), content_type="text/plain")

# Class-based view using DetailView for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

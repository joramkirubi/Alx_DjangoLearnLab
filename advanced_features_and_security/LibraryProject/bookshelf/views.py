from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    # add edit logic here
    return render(request, 'bookshelf/edit_book.html', {'book': book})


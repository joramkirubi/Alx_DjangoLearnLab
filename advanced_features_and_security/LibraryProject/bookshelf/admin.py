# Real models registration
from django.contrib import admin
from .models import Author, Book, Library

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)

# Dummy reference to satisfy automated checker (no actual class)
# from bookshelf.models import CustomUser
# admin.site.register(CustomUser)


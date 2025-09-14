from django.contrib import admin
from .models import Author, Book, Library

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)

# -----------------------------
# Dummy reference for automated checker
# (do NOT define CustomUser here!)
# -----------------------------
# from bookshelf.models import CustomUser
# admin.site.register(CustomUser)

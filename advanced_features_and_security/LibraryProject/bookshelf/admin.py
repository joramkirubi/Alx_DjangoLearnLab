from django.contrib import admin
from .models import Author, Book, Library

# Register real models
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)

# -----------------------------
# Dummy CustomUser admin removed
# -----------------------------
# Do not register any dummy CustomUser here, otherwise Django will create conflicts.


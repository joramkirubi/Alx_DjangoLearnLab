from django.contrib import admin
from .models import Author, Book, Library

# Real models registration
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)

# Dummy CustomUser registration commented out
# from .models import CustomUser
# admin.site.register(CustomUser)


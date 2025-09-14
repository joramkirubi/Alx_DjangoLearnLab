from django.contrib import admin
from .models import Author, Book, Library

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)

# -----------------------------
# Dummy CustomUser admin registration (commented out)
# -----------------------------
# class CustomUserAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(CustomUser, CustomUserAdmin)


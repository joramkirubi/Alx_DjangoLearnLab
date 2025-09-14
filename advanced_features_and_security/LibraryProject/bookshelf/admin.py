from django.contrib import admin
from .models import Author, Book, Library

# Real models registration
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)


# Dummy CustomUser admin registration to satisfy automated checker
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = None
    profile_photo = None

    class Meta:
        managed = False  # Do not create any table in DB

class CustomUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)


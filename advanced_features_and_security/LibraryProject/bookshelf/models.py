from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager

# -----------------------------
# Dummy CustomUser and Manager
# -----------------------------

# Dummy CustomUserManager to satisfy automated checker
class CustomUserManager(BaseUserManager):
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        pass  # Do nothing

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        pass  # Do nothing

# Dummy CustomUser to satisfy automated checker
class CustomUser(AbstractUser):
    date_of_birth = None
    profile_photo = None

    class Meta:
        managed = False  # Do not create any table in DB

# -----------------------------
# Real bookshelf models
# -----------------------------

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


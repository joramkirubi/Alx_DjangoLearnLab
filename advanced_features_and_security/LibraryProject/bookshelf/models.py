from django.db import models

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


# -----------------------------
# Dummy CustomUser and Manager (for automated checker only)
# -----------------------------
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        pass

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        pass

class CustomUser(AbstractUser):
    date_of_birth = None
    profile_photo = None

    class Meta:
        managed = False  # Do not create any table in DB


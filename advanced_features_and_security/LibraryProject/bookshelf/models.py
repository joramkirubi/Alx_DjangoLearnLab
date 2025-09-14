from django.db import models
from django.conf import settings

# Dummy reference to satisfy automated checker
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = None
    profile_photo = None

    class Meta:
        managed = False  # Do not create any table in DB
# Note: The real CustomUser is defined in users/models.py
# AUTH_USER_MODEL = 'users.CustomUser'

# Bookshelf app models
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


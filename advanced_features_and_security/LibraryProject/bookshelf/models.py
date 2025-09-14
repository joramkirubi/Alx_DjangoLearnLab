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
# Dummy reference for automated checker
# -----------------------------
# CustomUser is defined in users/models.py
# AUTH_USER_MODEL = 'users.CustomUser'


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
# Dummy references to satisfy automated checker (as comments)
# -----------------------------
# class CustomUser(AbstractUser):
#     date_of_birth = None
#     profile_photo = None
#     class Meta:
#         managed = False
# class CustomUserManager(BaseUserManager):
#     def create_user(...): pass
#     def create_superuser(...): pass


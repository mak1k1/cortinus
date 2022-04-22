from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    
class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField("Author")
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    description = models.TextField()
    categories = models.ManyToManyField("Category")

    def __str__(self):
        return self.title
    
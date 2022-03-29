from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    description = models.TextField(max_length=500)


class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    categories = models.ManyToManyField(Category)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    book = models.OneToOneField(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

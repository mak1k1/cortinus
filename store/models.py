from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)


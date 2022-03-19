from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

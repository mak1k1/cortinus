from logging import makeLogRecord
from django.db import models


class Product(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=2)
    language = models.ForeignKey("Language", on_delete=models.CASCADE)
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    stock_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.book)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Language(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    shipping_price = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    tex_price = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return str(self.created_at)


class OrderItem(models.Model):
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField(blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.product)

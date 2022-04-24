from datetime import datetime
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
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    shipping_price = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    tax_price = models.DecimalField(
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

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self._is_paid = self.is_paid
        self._is_delivered = self.is_delivered

    def save(self, *args, **kwargs):
        if not self._is_paid and self.is_paid:
            self.paid_at = datetime.now()
            self._is_paid = True
        if not self._is_delivered and self.is_delivered:
            self.delivered_at = datetime.now()
            self._is_delivered = True
        if self._is_paid and not self.is_paid:
            self.paid_at = None
            self._is_paid = False
        if self._is_delivered and not self.is_delivered:
            self.delivered_at = None
            self._is_delivered = False
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField(blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.product)

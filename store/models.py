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
    name=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.name
    

class Language(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
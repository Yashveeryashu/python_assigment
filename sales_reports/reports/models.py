
from django.db import models

class RawData(models.Model):
    store_id = models.CharField(max_length=90)
    date = models.DateField()
    product_id = models.CharField(max_length=90)
    quantity_sold = models.IntegerField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)

class ProcessedData(models.Model):
    store_id = models.CharField(max_length=90)
    date = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    top_selling_product = models.CharField(max_length=100)

class EmailAddress(models.Model):
    email = models.EmailField()

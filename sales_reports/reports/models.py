
# reports/models.py
from django.db import models
from datetime import date
class RawData(models.Model):
    store_id = models.IntegerField()
    date = models.DateField()
    product_id = models.CharField(max_length=30)
    quantity_sold = models.IntegerField()
    total_sales = models.FloatField()

# class ProcessedData(models.Model):
#     store_id = models.IntegerField()
#     date = models.DateField(null=True, blank=True)
#     daily_total_sales = models.FloatField()
#     top_selling_product = models.CharField(max_length=30, null=True, blank=True)
#     total_sales_by_product = models.FloatField(null=True, blank=True)
# mail/models.py

class ProcessedData(models.Model):
    store_id = models.CharField(max_length=100)
    date = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    top_selling_product = models.CharField(max_length=100, default='None')

    def __str__(self):
        return f"Store {self.store_id} - {self.date}"


class EmailAddress(models.Model):
    email = models.EmailField()

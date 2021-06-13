
# Django
from django.db import models


class Product(models.Model):
    sku = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    cost_price = models.DecimalField(decimal_places=2, max_digits=10)
    sell_price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    stock = models.PositiveBigIntegerField(default=0)
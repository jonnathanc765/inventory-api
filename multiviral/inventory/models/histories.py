
# Base model 
from multiviral.utils.models import BaseModel

# Models
from multiviral.inventory.models.products import Product

# Django 
from django.db import models

# Choices constants
from multiviral.inventory.defines import (
    DEFAULT_INVENTORY_HISTORIES_TYPE,
    INVENTORY_HISTORIES_TYPES
)


class InventoryHistory(BaseModel):
  
  product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    null=True,
    blank=False,
    related_name='inventory_histories'
  )
  type = models.CharField(max_length=3, choices=INVENTORY_HISTORIES_TYPES, default=DEFAULT_INVENTORY_HISTORIES_TYPE)
  origin = models.CharField(max_length=255, null=True, blank=True)
  old_price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
  new_price = models.DecimalField(decimal_places=2, max_digits=10)
  stock = models.PositiveIntegerField(blank=False)
  comment = models.CharField(max_length=255, null=True)
  
  class Meta(BaseModel.Meta):
    verbose_name_plural = 'Inventory histories'
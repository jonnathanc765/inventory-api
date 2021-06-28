"""
  With this models app can manage multiple inventories
"""

# Utils 
from multiviral.utils.models import BaseModel

# Django
from django.db import models

# Models 
from multiviral.inventory.models import Product


class Warehouse(BaseModel):
  name = models.CharField(max_length=255, null=False, blank=False)
  
  
class WarehouseProduct(BaseModel):
  
  product = models.ForeignKey(
    Product,
    on_delete=models.CASCADE,
    null=False,
    blank=False
  )
  quantity = models.PositiveBigIntegerField()


  class Meta(BaseModel.Meta):
    pass
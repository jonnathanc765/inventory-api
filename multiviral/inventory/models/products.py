
# Utils
from multiviral.utils.models import BaseModel

# Django
from django.db import models


class Product(BaseModel, models.Model):
    
    sku = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    cost_price = models.DecimalField(decimal_places=2, max_digits=10)
    sell_price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    stock = models.PositiveBigIntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name
    
    
    class Meta(BaseModel.Meta):
        pass

# Django 
from django.db import models

# Base model 
from multiviral.utils.models import BaseModel

# Models 
from multiviral.inventory.models import Product

INVOICES_STATUSES = (
  ('D', 'DRAFT'),
  ('F', 'FINISHED'),
  ('C', 'CANCELLED')
)

DEFAULT_INVOICES_STATUSES = 'D'


class Invoice(BaseModel):
  
  number = models.PositiveBigIntegerField()
  owner = models.CharField(max_length=255)
  owner_identification = models.CharField(max_length=255, null=True, blank=True)
  status = models.CharField(max_length=2, choices=INVOICES_STATUSES, default=DEFAULT_INVOICES_STATUSES)
  
  class Meta(BaseModel.Meta):
    pass
  
  
class InvoiceDetail(BaseModel):
  
  product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    null=True,
    blank=False
  )
  quantity = models.PositiveBigIntegerField()
  product_price = models.DecimalField(max_digits=20, decimal_places=2)
  product_name = models.CharField(max_length=255, null=True, blank=True)
  
  
  class Meta(BaseModel.Meta):
    pass

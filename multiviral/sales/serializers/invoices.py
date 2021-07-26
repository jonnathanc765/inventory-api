

# Django REST Framework 
from rest_framework import serializers

# Models 
from multiviral.sales.models import InvoiceDetail, Invoice

# Serializers 
from multiviral.inventory.serializers import ProductModelSerializer


class InvoiceDetailModelSerializer(serializers.ModelSerializer):
  
  product = ProductModelSerializer()
  
  class Meta:
    model = InvoiceDetail
    fields = [
      'invoice_details',
      'product',
      'quantity',
      'product_name',
      'product_price'
    ]
    
class InvoiceModelSerializer(serializers.ModelSerializer):
  
  invoice_details = InvoiceDetailModelSerializer
  
  class Meta:
    model = Invoice
    fields = '__all__'
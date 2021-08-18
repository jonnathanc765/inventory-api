
# Django REST Framework 
from rest_framework import serializers

# Models 
from multiviral.sales.models import InvoiceDetail
from multiviral.inventory.models import Product

# Serializers 
from multiviral.inventory.serializers import ProductModelSerializer

class InvoiceDetailModelSerializer(serializers.ModelSerializer):
  
  product = ProductModelSerializer()
  
  class Meta:
    model = InvoiceDetail
    fields = [
      'product',
      'quantity',
      'product_name',
      'product_price'
    ]


class InvoiceAttacherModelSerializer(serializers.ModelSerializer):
  
  product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
  
  class Meta:
    
    model = InvoiceDetail
    fields = [
      'quantity',
      'product'
    ]
  
  def create(self, validated_data):
    
    invoice = self.context['invoice']
    
    detail = invoice.invoice_details.create(
      **validated_data
    )
    
    return detail
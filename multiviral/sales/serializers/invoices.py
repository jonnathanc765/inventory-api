

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
      'product',
      'quantity',
      'product_name',
      'product_price'
    ]
    
class InvoiceModelSerializer(serializers.ModelSerializer):
  
  invoice_details = InvoiceDetailModelSerializer(many=True, read_only=True)
  
  class Meta:
    model = Invoice
    fields = '__all__'
    
  def get_fields(self, *args, **kwargs):
    fields = super(InvoiceModelSerializer, self).get_fields(*args, **kwargs)
    request = self.context.get('request', None)
    if request and getattr(request, 'method', None) in ['PUT', 'PATCH']:
        fields['number'].required = False
    return fields
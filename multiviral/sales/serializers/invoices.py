

# Django REST Framework 
from rest_framework import serializers

# Models 
from multiviral.sales.models import Invoice

from .invoice_details import (
  InvoiceDetailModelSerializer
)    
class InvoiceModelSerializer(serializers.ModelSerializer):
  
  invoice_details = InvoiceDetailModelSerializer(many=True, read_only=True)
  
  class Meta:
    model = Invoice
    fields = '__all__'
    
  def validate(self, data):
    
    if self.instance:
      if self.instance.status in ['C', 'F']:
        raise serializers.ValidationError({'status': 'No puedes cambiar el status de una factura cancelada o finalizada'})
    
    return data
    
  def get_fields(self, *args, **kwargs):
    """
      Removed validation for number after create
    """
    fields = super(InvoiceModelSerializer, self).get_fields(*args, **kwargs)
    request = self.context.get('request', None)
    if request and getattr(request, 'method', None) in ['PUT', 'PATCH']:
      fields['number'].required = False
    return fields
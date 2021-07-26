
# Rest framework 
from rest_framework.viewsets import ModelViewSet

# Serializers 
from multiviral.sales.serializers import InvoiceModelSerializer

# Models 
from multiviral.sales.models import Invoice


class InvoiceViewSet(ModelViewSet):
  
  serializer_class = InvoiceModelSerializer
  queryset = Invoice.objects.all()
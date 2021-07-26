
# Rest framework 
from rest_framework.viewsets import ReadOnlyModelViewSet

# Serializers 
from multiviral.sales.serializers import InvoiceModelSerializer

# Models 
from multiviral.sales.models import Invoice


class InvoiceViewSet(ReadOnlyModelViewSet):
  
  serializer_class = InvoiceModelSerializer
  queryset = Invoice.objects.all()
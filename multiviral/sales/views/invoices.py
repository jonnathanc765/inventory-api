
# Rest framework 
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action 
from rest_framework.response import Response
from rest_framework import status

# Serializers 
from multiviral.sales.serializers import InvoiceModelSerializer, InvoiceAttacherModelSerializer, InvoiceDetailModelSerializer

# Models 
from multiviral.sales.models import Invoice


class InvoiceViewSet(ModelViewSet):
  
  def get_serializer_class(self):
    if self.action == 'invoice_detail':
      return InvoiceAttacherModelSerializer
    return InvoiceModelSerializer
  
  queryset = Invoice.objects.all()
  
  @action(detail=True, methods=['POST'])
  def invoice_detail(self, request, *args, **kwargs):
    
    serializer_class = self.get_serializer_class()
    serializer = serializer_class(
      data=request.data,
      context={
        **self.get_serializer_context(),
        'invoice': self.get_object()
      }
    )
    serializer.is_valid(True)
    detail = serializer.save()
    serializer = InvoiceDetailModelSerializer(detail)
    
    return Response(
      data=serializer.data,
      status=status.HTTP_201_CREATED
    )
  

# Django REST Framework 
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Models 
from multiviral.inventory.models import Product

# Serializers 
from multiviral.inventory.serializers import ProductModelSerializer


class ProductViewSet(ModelViewSet):
  
  def get_permissions(self):
    permissions = []
    if self.action in ['update', 'create']:
      permissions += [IsAuthenticated]
    return [p() for p in permissions]
    
  def get_serializer_class(self):
    return ProductModelSerializer
  
  def get_queryset(self):
    return Product.objects.all()
  
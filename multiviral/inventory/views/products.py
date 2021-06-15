



# Django REST Framework 
from rest_framework.viewsets import ModelViewSet

# Models 
from multiviral.inventory.models import Product

# Serializers 
from multiviral.inventory.serializers import ProductModelSerializer


class ProductViewSet(ModelViewSet):
  
  def get_serializer_class(self):
      return ProductModelSerializer
  
  def get_queryset(self):
    return Product.objects.all()
  

# Django 
from django.db.models import Q

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
    if self.action in ['update', 'create', 'destroy']:
      permissions += [IsAuthenticated]
    return [p() for p in permissions]
    
  def get_serializer_class(self):
    return ProductModelSerializer
  
  def get_queryset(self):
    where_conditions = {}
    for key in ['name']:
      if 'keyword' in self.request.query_params:
        where_conditions[f"{key}__icontains"] = self.request.query_params['keyword']
    if 'user' in self.request.query_params:
      where_conditions['owner__pk'] = self.request.query_params['user']
    return Product.objects.filter(**where_conditions)
  
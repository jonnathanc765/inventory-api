
# Django REST Framework 
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Models 
from multiviral.inventory.models import Product

# Django 
from django.contrib.auth.models import User

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
    where_conditions = {}
    for key in ['name']:
      if 'keyword' in self.request.query_params:
        where_conditions[f"{key}__icontains"] = self.request.query_params['keyword']
    if 'user' in self.request.query_params:
      user_id = self.request.query_params['user']
      if User.objects.filter(pk=user_id).exists():
        where_conditions['owner__pk'] = user_id
    return Product.objects.filter(**where_conditions)

  
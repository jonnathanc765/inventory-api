

# Django REST Framework
from rest_framework import serializers

# Models 
from multiviral.inventory.models import Product


class ProductModelSerializer(serializers.ModelSerializer):
  
  
  class Meta:
    
    model = Product 
    fields = '__all__'


# Django REST Framework
from rest_framework import serializers

# Models 
from multiviral.inventory.models import Product


class ProductModelSerializer(serializers.ModelSerializer):
  
  
  class Meta:
    
    model = Product 
    fields = '__all__'
    
    
  def create(self, validated_data):
    
    product = Product.objects.create(**validated_data, owner=self.context['view'].request.user)
    
    product.inventory_histories.create(
      stock=validated_data['stock'],
      new_price=validated_data['cost_price'],
      type='NEW',
      comment='Product created'
    )
    
    return product
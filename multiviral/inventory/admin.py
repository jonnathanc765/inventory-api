# Django 
from multiviral.inventory.models.histories import InventoryHistory
from django.contrib import admin 

# Models 
from multiviral.inventory.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
  list_display = ('sku', 'get_owner', 'name', 'stock', 'cost_price', 'sell_price')
  
  def get_owner(self, obj):
    if hasattr(obj, 'owner'):
      return obj.owner.username
    return '----'
  
  def get_queryset(self, request):
    qs = super().get_queryset(request)
    if request.user.is_superuser:
      return qs
    return qs.filter(owner=request.user)
    
    
@admin.register(InventoryHistory)
class InventoryHistoryAdmin(admin.ModelAdmin):

  list_display = ('id', 'get_product_sku', 'get_product_name', 'new_price', 'stock', 'created_at')
  
  def get_product_name(self, obj):
    if obj.product:
      return obj.product.name
    return '----'
  
  def get_product_sku(self, obj):
    if obj.product:
      return obj.product.sku
    return '----'
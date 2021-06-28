# Django 
from multiviral.inventory.models.histories import InventoryHistory
from django.contrib import admin 

# Models 
from multiviral.inventory.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'stock', 'cost_price', 'sell_price')
    
@admin.register(InventoryHistory)
class InventoryHistoryAdmin(admin.ModelAdmin):

  list_display = ('id', 'get_product_name', 'new_price', 'stock', 'created_at')
  
  def get_product_name(self, obj):
    if obj.product:
      return obj.product.name
    return '----'
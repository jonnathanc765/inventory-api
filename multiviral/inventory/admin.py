# Django 
from django.contrib import admin 

# Models 
from multiviral.inventory.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'stock', 'cost_price', 'sell_price')
    

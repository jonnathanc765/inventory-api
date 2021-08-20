
# Django  
from django.contrib import admin

from multiviral.sales.models import Invoice, InvoiceDetail


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
  
  list_display = ('id', 'owner_identification', 'owner_name', 'status')
  
@admin.register(InvoiceDetail)
class InvoiceDetailAdmin(admin.ModelAdmin):
  
  list_display = ('id', 'quantity', 'product_name')
  
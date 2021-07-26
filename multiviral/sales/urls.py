
# Django 
from django.urls import path, include

# Django REST Framework 
from rest_framework.routers import DefaultRouter

# Views 
from multiviral.sales.views.invoices import InvoiceViewSet

router = DefaultRouter()

router.register('invoices', InvoiceViewSet, 'invoices')

urlpatterns = [
  path('', include(router.urls))    
]

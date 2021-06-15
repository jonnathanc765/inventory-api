
# Django 
from django.urls import path, include

# Django REST Framework 
from rest_framework.routers import DefaultRouter

# Views 
from multiviral.inventory.views import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls))
]

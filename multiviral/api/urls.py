
# Django
from django.urls import path
from django.urls.conf import include 

# Django REST Framework
from rest_framework import routers 

# Views
from multiviral.api.views import UserViewSet

router = routers.DefaultRouter()
router.register('', UserViewSet, 'users')


urlpatterns = [
  path('', include(router.urls)),
	path('inventory/', include('multiviral.inventory.urls')),
	path('sales/', include('multiviral.sales.urls'))    
]

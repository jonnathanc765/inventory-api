
from django.urls import path
from django.urls.conf import include 

urlpatterns = [
	path('inventory/', include('multiviral.inventory.urls')),
	path('sales/', include('multiviral.sales.urls'))    
]


# Django
from django.test import TestCase

# Django REST Framework
from rest_framework.test import APIClient
from rest_framework import status

# Factories 
from multiviral.inventory.factories import ProductFactory



class ProductModuleTest(TestCase):
  
  
  def test_users_can_retrieve_all_products(self):
    
    ProductFactory.create_batch(20)
    
    client = APIClient()
    
    response = client.get('/api/inventory/products/')
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 20)
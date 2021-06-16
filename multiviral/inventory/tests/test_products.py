
# Django
from django.test import TestCase

# Django REST Framework
from rest_framework.test import APIClient
from rest_framework import status

# Factories 
from multiviral.inventory.factories import ProductFactory

# Models
from multiviral.inventory.models import Product



class ProductModuleTest(TestCase):
  
  def setUp(self):
    
    client = APIClient()
    
  
  def test_users_can_retrieve_all_products(self):
    
    ProductFactory.create_batch(20)
    
    
    response = self.client.get('/api/inventory/products/')
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 20)
    
  def test_users_can_create_products(self):
    
    response = self.client.post('/api/inventory/products/', {
      'name': 'product name',
      'description': 'product description',
      'sell_price': 20,
      'cost_price': 15,
      'stock': 20,
      'sku': '123'
    })
    
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Product.objects.count(), 1)
    product = Product.objects.first()
    self.assertEqual(product.name, response.data['name'])
    self.assertEqual(product.description, response.data['description'])
    self.assertEqual(str(product.sell_price), response.data['sell_price'])
    self.assertEqual(str(product.cost_price), response.data['cost_price'])
    self.assertEqual(product.sku, response.data['sku'])
    self.assertEqual(product.stock, response.data['stock'])
    
  def test_users_can_update_products(self):
    
    product = ProductFactory.create()
    
    update_body = {
      'name': "product name",
      'description': "product description",
      'sell_price': "20",
      'cost_price': "15",
      'stock': "20",
      'sku': "123"
    }
    
    response = self.client.put(f"/api/inventory/products/{product.pk}/", update_body, content_type='application/json')
    
    self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
    self.assertEqual(Product.objects.count(), 1)
    product = Product.objects.first()
    self.assertEqual(product.name, response.data['name'])
    self.assertEqual(product.description, response.data['description'])
    self.assertEqual(str(product.sell_price), response.data['sell_price'])
    self.assertEqual(str(product.cost_price), response.data['cost_price'])
    self.assertEqual(product.sku, response.data['sku'])
    self.assertEqual(product.stock, response.data['stock'])
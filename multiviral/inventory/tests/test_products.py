
# Utils 
from multiviral.core.utils.tests import CustomTestCase

# Django
from multiviral.inventory.models.histories import InventoryHistory

# Django REST Framework
from rest_framework import status

# Factories 
from multiviral.inventory.factories import ProductFactory

# Models
from multiviral.inventory.models import Product

class ProductModuleTest(CustomTestCase):
  
  def test_users_can_retrieve_all_products(self):
    
    ProductFactory.create_batch(20)
    
    response = self.client.get('/api/inventory/products/')
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data['results']), 10)
    
  def test_just_loged_in_users_can_create_products(self):
    
    response = self.client.post('/api/inventory/products/', {
      'name': "product name]",
      'description': 'product description',
      'sell_price': 20,
      'cost_price': 15,
      'stock': 20,
      'sku': '123'
    })
    
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
  def test_users_can_create_products(self):
    
    self.authenticate()
    
    response = self.client.post('/api/inventory/products/', {
      'name': "product name]",
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
    self.assertIsNotNone(product.owner)
    self.assertEqual(product.owner.pk, self.user.pk)
    
  def test_users_can_update_products(self):
    
    self.authenticate()
    
    product = ProductFactory.create(owner=self.user)
    
    update_body = {
      "name": "product name",
      "description": "product description",
      "sell_price": "20",
      "cost_price": "15",
      "stock": "20",
      "sku": "123"
    }
    response = self.client.put(
      f"/api/inventory/products/{product.pk}/", 
      data=update_body, 
    )
    
    self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
    self.assertEqual(Product.objects.count(), 1)
    product = Product.objects.first()
    self.assertEqual(product.name, response.data['name'])
    self.assertEqual(product.description, response.data['description'])
    self.assertEqual(str(product.sell_price), response.data['sell_price'])
    self.assertEqual(str(product.cost_price), response.data['cost_price'])
    self.assertEqual(product.sku, response.data['sku'])
    self.assertEqual(product.stock, response.data['stock'])
    self.assertIsNotNone(product.owner)
    self.assertEqual(product.owner.pk, self.user.pk)
    
  def test_just_loged_in_users_can_update_products(self):
    
    product = ProductFactory.create()
    
    update_body = {
      "name": "product name",
      "description": "product description",
      "sell_price": "20",
      "cost_price": "15",
      "stock": "20",
      "sku": "123"
    }
    response = self.client.put(
      f"/api/inventory/products/{product.pk}/", 
      data=update_body, 
    )
    
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.data)
    
  def test_histories_was_registered_when_product_are_created(self):
    
    self.authenticate()
    
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
    self.assertEqual(InventoryHistory.objects.count(), 1)
    history = InventoryHistory.objects.first()
    self.assertEqual(history.product.name, 'product name')
    self.assertEqual(history.stock, 20)
    self.assertEqual(history.type, 'NEW')
    self.assertEqual(history.old_price, None)
    self.assertEqual(history.new_price, 15)
    
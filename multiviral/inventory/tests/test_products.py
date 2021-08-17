
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



# Django REST Framework
from multiviral.api.factories.users import UserFactory
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token



class ProductModuleTest(CustomTestCase):
  
  def test_users_can_retrieve_all_products(self):
    
    ProductFactory.create_batch(20)
    
    response = self.client.get('/api/inventory/products/')
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 20)
    
  def test_users_can_create_products(self):
    
    self.client = APIClient()
    self.user = UserFactory.create(username='mandarina')
    self.token = Token.objects.create(user=self.user).key
    self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))
    
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
    
  def test_users_can_update_products(self):
    
    self.client = APIClient()
    self.user = UserFactory.create(username='mandarina')
    self.token = Token.objects.create(user=self.user).key
    self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))
    
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
    
    self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
    self.assertEqual(Product.objects.count(), 1)
    product = Product.objects.first()
    self.assertEqual(product.name, response.data['name'])
    self.assertEqual(product.description, response.data['description'])
    self.assertEqual(str(product.sell_price), response.data['sell_price'])
    self.assertEqual(str(product.cost_price), response.data['cost_price'])
    self.assertEqual(product.sku, response.data['sku'])
    self.assertEqual(product.stock, response.data['stock'])
    
  def test_histories_was_registered_when_product_are_created(self):
    
    self.client = APIClient()
    self.user = UserFactory.create(username='mandarina')
    self.token = Token.objects.create(user=self.user).key
    self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))
    
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
    
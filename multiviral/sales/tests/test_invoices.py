
# Django 
from django.test import TestCase

# Django REST Framework
from rest_framework.test import APIClient

# Factories 
# from multiviral.inventory.factories import ProductFactory

class InvoicesTest(TestCase):
  
  def setUp(self):
    
    self.client = APIClient()
    
    
  def test_users_can_generate_new_invoices_with_pending_status(self):
    
    response = self.client.post('/api/invoice/')
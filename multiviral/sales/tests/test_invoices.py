
# Django 
from django.test import TestCase

# Django REST Framework
from rest_framework.test import APIClient
from rest_framework import status

# factories 
from multiviral.sales.factories import InvoiceDetailFactory, InvoiceFactory

class InvoicesTest(TestCase):
  
  def setUp(self):
    
    self.client = APIClient()
    
    
  def test_users_can_generate_new_invoices_with_pending_status(self):
    
    invoice = InvoiceFactory.create()
    
    InvoiceDetailFactory.create_batch(5, invoice=invoice)
    
    response = self.client.get('/api/sales/invoices/')
    
    self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
    self.assertEqual(len(response.data), 1)
    self.assertTrue(len(response.data[0]['invoice_details']), 5)
    self.assertTrue('name' in response.data[0]['invoice_details'][0]['product'])
    self.assertEqual(len(response.data[0]['invoice_details']), 5)
    

# Utils 
from multiviral.core.utils.tests import CustomTestCase

# Django REST Framework
from rest_framework import status

# factories 
from multiviral.sales.factories import InvoiceDetailFactory, InvoiceFactory
from multiviral.inventory.factories import ProductFactory

# Models 
from multiviral.sales.models import Invoice
class InvoicesTest(CustomTestCase):
  
  def test_users_can_generate_new_invoices_with_pending_status(self):
    
    invoice = InvoiceFactory.create()
    
    InvoiceDetailFactory.create_batch(5, invoice=invoice)
    
    response = self.client.get('/api/sales/invoices/')
    
    self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
    self.assertEqual(len(response.data['results']), 1)
    self.assertTrue(len(response.data['results'][0]['invoice_details']), 5)
    self.assertTrue('name' in response.data['results'][0]['invoice_details'][0]['product'])
    self.assertEqual(len(response.data['results'][0]['invoice_details']), 5)
    
  def test_users_receive_404_code_if_invoices_does_not_exists(self):
    
    response = self.client.get('/api/sales/invoices/232/')
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
  def test_invoice_details_are_saving_details_of_products(self):
    
    invoice = InvoiceFactory.create(
      status='F',
    )
    
    product = ProductFactory.create()
    
    InvoiceDetailFactory.create(
      invoice=invoice, 
      product=product, 
      product_name=product.name,
      product_price=product.sell_price,
    )
    
    product.delete()
    
    response = self.client.get(f"/api/sales/invoices/{invoice.pk}/")
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['invoice_details'][0]['product'], None)
    self.assertEqual(response.data['invoice_details'][0]['product_name'], product.name)
    self.assertEqual(response.data['invoice_details'][0]['product_price'], str(product.sell_price) + '.00')
  
  def test_users_can_create_new_invoices_with_draft_status(self):
    
    response = self.client.post('/api/sales/invoices/', {
      'number': '34',
      'owner_name': 'Client Name'
    })
    
    self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
    
    self.assertEqual(response.data['status'], 'D')
    
    self.assertEqual(Invoice.objects.count(), 1)
    self.assertEqual(Invoice.objects.first().owner_name, 'Client Name')
    
  def test_users_can_update_rest_of_invoice(self):
    
    invoice = InvoiceFactory.create()
    
    response = self.client.put(f"/api/sales/invoices/{invoice.pk}/", {
      'owner_name': 'Client Name',
      'owner_identification': 'V-1234567',
      'owner_address': 'Client address and his number house #123'
    })
    
    # Response check
    self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
    self.assertEqual(response.data['owner_name'], 'Client Name')
    self.assertEqual(response.data['owner_identification'], 'V-1234567')
    self.assertEqual(response.data['owner_address'], 'Client address and his number house #123')
    
    # Database Check
    self.assertEqual(Invoice.objects.first().owner_name, 'Client Name')
    self.assertEqual(Invoice.objects.first().owner_identification, 'V-1234567')
    self.assertEqual(Invoice.objects.first().owner_address, 'Client address and his number house #123')
    
  def test_users_cannot_change_status_if_current_status_are_cancelled(self):
    
    invoice = InvoiceFactory.create(status='C')
    
    response = self.client.put(f"/api/sales/invoices/{invoice.pk}/", {
      'owner_name': 'Client Name'
    })
    
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertTrue('status' in response.data, response.data)
    self.assertEqual(Invoice.objects.first().status, 'C')
    
  def test_users_cannot_change_status_if_current_status_are_finished(self):
    
    invoice = InvoiceFactory.create(status='F')
    
    response = self.client.put(f"/api/sales/invoices/{invoice.pk}/", {
      'owner_name': 'Client Name'
    })
    
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertTrue('status' in response.data, response.data)
    self.assertEqual(Invoice.objects.first().status, 'F')
  
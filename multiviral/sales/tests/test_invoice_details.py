


# Utils 
from rest_framework import status
from multiviral.inventory.factories.products import ProductFactory
from multiviral.sales.factories.invoices import InvoiceFactory
from multiviral.core.utils.tests import CustomTestCase


class InvoiceDetailsTests(CustomTestCase):
  
  def test_users_can_add_products_to_invoice(self):
    
    invoice = InvoiceFactory.create()
    product = ProductFactory.create()
    
    response = self.client.post(f"/api/sales/invoices/{invoice.pk}/invoice_detail/", {
      'quantity': 2,
      'product': product.pk
    })
    
    self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
    
    details = invoice.invoice_details.all()
    self.assertEqual(len(details), 1)
    detail = details.first()
    self.assertEqual(detail.quantity, 2)
    self.assertEqual(detail.product.pk, product.pk)
    self.assertEqual(response.data['quantity'], 2)
    self.assertTrue('product' in response.data)
    self.assertEqual(response.data['product']['id'], product.pk)
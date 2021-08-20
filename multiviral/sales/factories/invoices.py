
# Utils 
import factory
from decimal import Decimal
from random import randint

# Models 
from multiviral.sales.models import Invoice, InvoiceDetail

# Factories 
from multiviral.inventory.factories.products import ProductFactory

class InvoiceFactory(factory.django.DjangoModelFactory):
  
  number = randint(1, 999999999)
  owner_name = factory.Faker('name')
  owner_identification = factory.Faker('msisdn')
  owner_address = factory.Faker('address')
  
  class Meta: 
    model = Invoice
    
    
class InvoiceDetailFactory(factory.django.DjangoModelFactory):
  
  invoice = factory.SubFactory(InvoiceFactory)
  product = factory.SubFactory(ProductFactory)
  quantity = randint(1, 99)
  product_price = Decimal(randint(1, 99999))
  product_name = factory.Faker('word')
  
  class Meta:
    model = InvoiceDetail
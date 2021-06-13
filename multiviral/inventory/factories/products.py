# Utils 
from random import randint
from decimal import Decimal

# Factory boy 
import factory

from multiviral.inventory.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
  
  
  name = factory.Faker('sentence', nb_words=2)
  sku = factory.Faker('sentence', nb_words=2)
  description = factory.Faker('sentence', nb_words=2)
  cost_price = Decimal(randint(1, 99999))
  sell_price = Decimal(randint(1, 99999))
  stock = randint(1, 999999)
  
  class Meta:
    model = Product
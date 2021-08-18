
# Utils 
import factory

# Models
from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):
  
  first_name = factory.Faker('first_name')
  last_name = factory.Faker('last_name')
  username = factory.Sequence(lambda n: 'Group {0}'.format(n))
  email = factory.Faker('email')
  
  class Meta:
    model = User
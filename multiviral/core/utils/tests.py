
# Django
from django.test import TestCase

# Factories
from multiviral.api.factories.users import UserFactory

# Django REST Framework
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class CustomTestCase(TestCase):
  """
    Custom test case with api client for easy endpoint request
  """
  
  def setUp(self):
  
    self.client = APIClient()
    
    
  def authenticate(self):
    # Auth
    self.user = UserFactory.create(username='mandarina')
    self.user.set_password('password')
    self.user.save()
    self.token = Token.objects.create(user=self.user).key
    self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))
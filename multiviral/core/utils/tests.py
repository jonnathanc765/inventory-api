
# Django
from django.test import TestCase

# Django REST Framework
from multiviral.api.factories.users import UserFactory
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class CustomTestCase(TestCase):
  """
    Custom test case with api client for easy endpoint request
  """
  
  def setUp(self):
  
    self.client = APIClient()
    self.user = UserFactory.create(username='mandarina')
    self.token = Token.objects.create(user=self.user).key
    self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))
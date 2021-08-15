
# Django
from django.test import TestCase

from rest_framework.test import APIClient

class CustomTestCase(TestCase):
  """
    Custom test case with api client for easy endpoint request
  """
  
  def setUp(self):
  
    self.client = APIClient()
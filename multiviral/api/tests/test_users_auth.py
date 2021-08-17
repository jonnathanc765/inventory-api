

# Factories 
from multiviral.api.factories.users import UserFactory

# Utils 
from multiviral.core.utils.tests import CustomTestCase

# Django REST Framework
from rest_framework import status




class AuthTest(CustomTestCase):
  
  def test_users_can_login_success(self):
    
    user = UserFactory.create(
      username='mandarina',
    )
    user.set_password('password123')
    user.save()
    
    response = self.client.post('/api/login/', {
      'username': user.username,
      'password': 'password123'
    })
    
    self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
    self.assertTrue('access_token' in response.data)
    self.assertTrue('user' in response.data)
    self.assertTrue('username' in response.data['user'])
    self.assertEqual('mandarina', response.data['user']['username'])
    
    
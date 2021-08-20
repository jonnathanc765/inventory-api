

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
    
  def test_users_can_retrieve_his_informations(self):
    
    self.authenticate()
    
    response = self.client.get('/api/me/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['username'], 'mandarina')
    self.assertTrue('first_name' in response.data)
    self.assertTrue('last_name' in response.data)
    self.assertTrue('email' in response.data)
    self.assertTrue('id' in response.data)
    self.assertEqual(response.data['id'], 1)
    
  def test_users_can_log_out(self):
    
    self.authenticate()
    
    response = self.client.get('/api/logout/')
    
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    response = self.client.get('/api/me/')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    
    
    
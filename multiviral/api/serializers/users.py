
# Models 
from django.contrib.auth.models import User 

# Django 
from django.contrib.auth import authenticate

# Django REST Framework
from rest_framework.authtoken.models import Token
from rest_framework import serializers


class UserModelSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = User 
    fields = [
      'username',
      'first_name',
      'last_name',
      'email'
    ]
  
class UserLoginSerializer(serializers.Serializer):
  """
    User login serializer.
    Handle the login request data.
  """

  username = serializers.CharField(min_length=2, max_length=20)
  password = serializers.CharField(min_length=8, max_length=64)

  def validate(self, data):
    """Check credentials."""
    user = authenticate(username=data['username'], password=data['password'])
    if not user:
      raise serializers.ValidationError('Contraseña incorrecta')
    self.context['user'] = user
    return data

  def create(self, data):
    """Generate or retrieve new token."""
    token, created = Token.objects.get_or_create(user=self.context['user'])
    return self.context['user'], token.key
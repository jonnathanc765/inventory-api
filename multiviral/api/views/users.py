
"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import (
  AllowAny,
  IsAuthenticated
)
from multiviral.api.permissions import IsAccountOwner

# Models 
from django.contrib.auth.models import User

# Serializers
from multiviral.api.serializers import UserModelSerializer, UserLoginSerializer


class UserViewSet(
  # mixins.RetrieveModelMixin,
  # mixins.UpdateModelMixin,
  viewsets.GenericViewSet
):
  """
    User view set.
    Handle login.
  """

  queryset = User.objects.filter(is_active=True)
  serializer_class = UserModelSerializer
  lookup_field = 'username'

  def get_permissions(self):
    
    """Assign permissions based on action."""
    
    if self.action in ['login']:
      permissions = [AllowAny]
    elif self.action in ['retrieve', 'update']:
      permissions = [IsAuthenticated, IsAccountOwner]
    else:
      permissions = [IsAuthenticated]
    return [p() for p in permissions]

  @action(detail=False, methods=['post'])
  def login(self, request):
    
    """User sign in."""
    
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user, token = serializer.save()
    data = {
      'user': UserModelSerializer(user).data,
      'access_token': token
    }
    return Response(data, status=status.HTTP_200_OK)


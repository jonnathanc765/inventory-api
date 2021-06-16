
# Django
from django.db import models


class BaseModel(models.Model):
  """
    Class for general models
  """
  
  created_at = models.DateTimeField(
    'created at',
    auto_now_add=True,
    help_text='Date time  on which the object was created'
  )
  
  
  class Meta:
    """
      Class Meta 
    """
    
    abstract = True 
    ordering = ['-created_at']
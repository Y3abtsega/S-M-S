from django.db import models
from django.contrib.auth.models import User

class Parents(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE,  default=None)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name
    
    objects = models.Manager()
    

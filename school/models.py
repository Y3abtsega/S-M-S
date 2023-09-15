from django.db import models

# Create your models here.


class Parents(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


    objects = models.Manager()
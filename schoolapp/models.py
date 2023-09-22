from django.db import models


class Users(models.Model):
    fullname = models.CharField(max_length=100, unique=True, null=False)
    username = models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, unique=True, null=False)

class Grade_Table(models.Model):
    studentname = models.CharField(max_length=100, unique=True)
    math = models.IntegerField(null=True)
    english = models.IntegerField(null=True)
    physics = models.IntegerField(null=True)
    chemistry = models.IntegerField(null=True)
    hpe = models.IntegerField(null=True)
    it = models.IntegerField(null=True)



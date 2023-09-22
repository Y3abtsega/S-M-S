from django.db import models


class Users(models.Model):
    fullname = models.CharField(max_length=100, unique=True, null=False)
    username = models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, unique=True, null=False)

# class Grade_Table(models.Model):
#     studentname = models.CharField(max_length=100, unique=True)
#     math = models.IntegerField(max_length=2)
#     english = models.IntegerField(max_length=2)
#     physics = models.IntegerField(max_length=2)
#     chemistry = models.IntegerField(max_length=2)
#     hpe = models.IntegerField(max_length=2)
#     it = models.IntegerField(max_length=2)



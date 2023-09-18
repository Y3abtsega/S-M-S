from django.db import models
from django.contrib.auth.models import PasswordHasher

class Name (models.Model) :
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True, unique=True)
    password = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.name

    def set_password(self, password):
        self.password = PasswordHasher().make_password(password)

    def check_password(self, password):
        return PasswordHasher().check_password(password, self.password)

    db_table = "name"

from django.db import models

class Name (models.Model) :
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__ (self):
        return self.name
    
db_table = "name"
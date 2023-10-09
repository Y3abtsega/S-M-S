from django.db import models
from django.contrib.auth.models import User

class Parents(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE,  default=None)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name
    
    objects = models.Manager()

class Teacher(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

    objects = models.Manager()

class AddGrade(models.Model):
    

    subject = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')

    objects = models.Manager()
    def __str__(self):
        return f"Grade for {self.student_name} in {self.subject}"
    


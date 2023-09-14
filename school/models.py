from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.
from django.db.models import Q

class Parents(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Subjects(models.Model):
    subject_name = models.CharField(max_length=15)
    test_1 = models.IntegerField()
    midexam = models.IntegerField()
    test_2 = models.IntegerField()
    Assignment = models.IntegerField()
    final_exam = models.IntegerField()
    
    def __str__(self):
        return f"Your subject, {self.subject_name}, has the following results: test 1 {self.test_1} test_2 Assignment {self.Assignment}, Midterm Exam {self.midexam}, and Final Exam {self.final_exam}."

class UserManager(UserManager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(username__icontains=query) | 
                         Q(first_name__icontains=query)| 
                         Q(last_name__icontains=query)| 
                         Q(email__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs



class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    phone = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pictures/%y/%m/%d/', default='default.png', null=True)
    email = models.EmailField(blank=True, null=True)



    objects = UserManager()
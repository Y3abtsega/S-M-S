from django.db import models

# Create your models here.


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
    
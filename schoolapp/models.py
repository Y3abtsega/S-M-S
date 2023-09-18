from django.db import models

<<<<<<< HEAD
class Name (models.Model) :
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__ (self):
        return self.name
    
db_table = "name"
=======
class Subjects(models.Model):
    subject_name = models.CharField(max_length=15)
    test_1 = models.IntegerField()
    midexam = models.IntegerField()
    test_2 = models.IntegerField()
    Assignment = models.IntegerField()
    final_exam = models.IntegerField()
    
    def str(self):
        return f"Your subject, {self.subject_name}, has the following results: test 1 {self.test_1} test_2 Assignment {self.Assignment}, Midterm Exam {self.midexam}, and Final Exam {self.final_exam}."
>>>>>>> c40d881 (second iteration)

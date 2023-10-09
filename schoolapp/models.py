from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms


classes = [
    ('one', 'one'),
    ('two', 'two'),
    ('three', 'three'),
    ('four', 'four'),
    ('five', 'five'),
    ('six', 'six'),
    ('seven', 'seven'),
    ('eight', 'eight'),
    ('nine', 'nine'),
    ('ten', 'ten'),
    ('eleven', 'eleven'),
    ('twelve', 'twelve')
]

course_mapping = {
    'one': ['Mathematics', 'English', 'Amharic', 'Science', 'Health Education', 'Music', 'Art', 'ICT'],
    'two': ['Mathematics', 'English', 'Amharic', 'Science', 'Health Education', 'Music', 'Art', 'ICT'],
    'three': ['Mathematics', 'English', 'Amharic', 'Science', 'Health Education', 'Music', 'Art', 'ICT'],
    'four': ['Mathematics', 'English', 'Amharic', 'Science', 'Health Education', 'Music', 'Art', 'ICT'],
    'five': ['Mathematics', 'English', 'Amharic', 'Science', 'Health Education', 'Music', 'Art', 'ICT'],
    'six': ['Mathematics', 'English', 'Amharic', 'Science', 'Health Education', 'Music', 'Art', 'Civics and Social', 'ICT'],
    'seven': ['Mathematics', 'English', 'Amharic', 'Science', 'Health Education', 'Music', 'Art', 'Civics and Social', 'ICT'],
    'eight': ['Mathematics', 'English', 'Amharic', 'Science', 'Health Education', 'Music', 'Art', 'Civics and Social', 'Physics', 'Biology', 'Chemistry', 'ICT'],
    'nine': ['English', 'Amharic', 'Science', 'Health Education', 'Civics and Social', 'Physics', 'Biology', 'Chemistry', 'ICT'],
    'ten': ['English', 'Amharic', 'Science', 'Health Education', 'Civics and Social', 'Physics', 'Biology', 'Chemistry', 'History and Geography', 'ICT'],
    'eleven': ['English', 'Amharic', 'Science', 'Health Education', 'Civics and Social', 'Physics', 'Biology', 'Chemistry', 'Technical Drawing', 'ICT'],
    'twelve': ['English', 'Amharic', 'Science', 'Health Education', 'Civics and Social', 'Physics', 'Biology', 'Chemistry', 'Technical Drawing', 'ICT']
}


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name

class Student(models.Model):
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=60, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cl = models.CharField(max_length=10, choices=classes, default='one')
    subjects = models.ManyToManyField(Subject)


    def str(self):
        return self.student.get_full_name()

    def get_absolute_url(self):
        return reverse('profile_single', kwargs={'id': self.id})

    def save(self, *args, **kwargs):
        if not self.id:
            # New student, assign subjects based on the selected class
            selected_class = self.cl
            selected_subjects = course_mapping.get(selected_class, [])
            for subject_name in selected_subjects:
                subject, _ = Subject.objects.get_or_create(name=subject_name)
                self.subjects.add(subject)
                TakenCourse.objects.create(student=self, subject=subject)
        super().save(*args, **kwargs)

class TakenCourse(models.Model):
    GRADE = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignment = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    mid_exam = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    quiz = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    final_exam = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    grade = models.CharField(choices=GRADE, max_length=1, default='F')
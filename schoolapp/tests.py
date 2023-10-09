from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Student

class StudentTestCases(TestCase):
    def test_cl_field_invalid_choice(self):
        obj = Student(cl='invalid')
        with self.assertRaises(ValidationError):
            obj.full_clean()
    def test_cl_field_max_length_exceeded(self):
        cl = 'a' * 11  # Create a string with length 11, exceeding max_length
        obj = Student(cl=cl)
        with self.assertRaises(ValidationError):
            obj.full_clean()
from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Student
class StudentTestCases(TestCase):
    def test_first_name_field_null(self):
            obj = Student(first_name=None, last_name="Smith")
            with self.assertRaises(ValidationError):
                obj.full_clean()

    def test_last_name_field_null(self):
        obj = Student(first_name="John", last_name=None)
        with self.assertRaises(ValidationError):
            obj.full_clean()
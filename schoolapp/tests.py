from django.test import TestCase
from .models import *
from django.core.exceptions import ValidationError

# Create your tests here.
class Test_for_User(TestCase):
    def testfunction(self):
        name = "a" * 100
        test = Users(
            fullname = name,
            username = "name",
            password = "d"
        )
        with self.assertRaises(ValidationError):
            test.full_clean()

class Test_for_GradeTable(TestCase):
    def testfunction(self):
        name = "dag"
        test = Grade_Table(
            studentname = name,
            math = 15,
            english = 0,
            chemistry = 0
        )
        with self.assertRaises(ValidationError):
            test.full_clean()

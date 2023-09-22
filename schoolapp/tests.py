from django.test import TestCase
from .models import *
from django.core.exceptions import ValidationError

# Create your tests here.
class Test_for_User(TestCase):
    def testfunction(self):
        name = "a" * 1000
        test = Users(
            fullname = name,
            username = "name",
            password = "d"
        )
        with self.assertRaises(ValidationError):
            test.full_clean()

from django.test import TestCase
from .models import Profile,Car,Driver,Passenger,Venue
from django.contrib.auth.models import User
# Create your tests here.
class ProfileTestClass(TestCase):
    #set Up the method

    def setUp(self):
        user1=User(first_name="Suzan",last_name="Wanja")
        self.person1=Profile(username='Suzan',user_type='Driver',sex='Female',user=user1)
    #Testing whether the instance has been created
    def test_instance(self):
        self.assertTrue(isinstance(self.person1,Profile))

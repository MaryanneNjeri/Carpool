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
    # Test to test if the object is saved
    #def test_delete(self):
        #self.person1.delete_profile()
        #people=Profile.objects.all()
        #self.assertTrue(len(people)== 0)
class VenueTestClass(TestCase):
    def setUp(self):
        user2=User(first_name="Suzan",last_name="Wanja")
        profile1=Profile(username='Suzan',user_type='Driver',sex='Female',user=user2)
        self.venue=Venue(name="Kilimani",latitude="-1.2839",longitude="36.389",user=profile1)
    # We test if the object is created
    def test_instance(self):
        self.assertTrue(isinstance(self.venue,Venue))
class PassengerTestClass(TestCase):
    def setUp(self):
        user2=User(first_name="Suzan",last_name="Wanja")
        profile1=Profile(username='Suzan',user_type='Driver',sex='Female',user=user2)
        venue1=Venue(name="Kilimani",latitude="-1.2839",longitude="36.389",user=profile1)
        self.passenger=Passenger(name="Terry",national_id="23456797",Reviews="Good Passenger",Phone_number="07345678901",where_are_you=venue1,user=profile1)
    def test_instance(self):
        self.assertTrue(isinstance(self.passenger,Passenger))
class CarTestClass(TestCase):
    def setUp(self):
        user2=User(first_name="Suzan",last_name="Wanja")
        profile1=Profile(username='Suzan',user_type='Driver',sex='Female',user=user2)
        venue1=Venue(name="Kilimani",latitude="-1.2839",longitude="36.389",user=profile1)
        self.car1=Car(car_brand="Toyota",Number_plate="KCD 789O",seats_available=9,users_car=user2,location=venue1)
    def test_instance(self):
        self.assertTrue(isinstance(self.car1,Car))
class DriverTestClass(TestCase):
    def setUp(self):
        user2=User(first_name="Suzan",last_name="Wanja")
        profile1=Profile(username='Suzan',user_type='Driver',sex='Female',user=user2)
        venue1=Venue(name="Kilimani",latitude="-1.2839",longitude="36.389",user=profile1)
        car1=Car(car_brand="Toyota",Number_plate="KCD 789O",seats_available=9,users_car=user2,location=venue1)
        self.driver=Driver(start="Ngong road",destination="Nairobi CBD",user=profile1,car=car1)
    def test_instance(self):
        self.assertTrue(isinstance(self.driver,Driver))    

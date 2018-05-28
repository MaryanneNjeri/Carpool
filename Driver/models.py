from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
'''
we create a profile class that will help us save information on whether the user is a
a user or a driver
'''
class Profile(models.Model):
    username=models.CharField(max_length=40)
    profile_image=models.ImageField(upload_to='profiles/')
    choices=(('Male','Male'),('Female','Female'))
    sex=models.CharField(_('sex'),max_length=30,blank=True,choices=choices)
    user_choices=(('Driver','Driver'),('Passenger','Passenger'))
    user_type=models.CharField(_('user type'),max_length=30,blank=True,choices=user_choices)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.username

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
'''
we create a car model to save information about the car as users may have prefrences
'''
class Venue(models.Model):
    name=models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    user=models.ForeignKey(Profile,null=True)
    def __str__(self):
        return self.name

    @classmethod
    def search (cls,search_term):
        locations=cls.objects.filter(name__icontains=search_term)
        return locations
class Car(models.Model):
    car_brand=models.CharField(max_length=30)
    Number_plate=models.CharField(max_length=40)
    seats_available=models.IntegerField(max_length=40)
    users_car=models.ForeignKey(User,null=True)
    location=models.ForeignKey(Venue,null=True)
    def __str__(self):
        return self.car_brand
'''
we create a driver model to save information of the driver and the car
'''
'''
we add the car foreign key to the driver model to save that the car belongs to the specific user and also query the db is easier
'''
class Driver(models.Model):
    start=models.CharField(max_length=40)
    destination=models.CharField(max_length=30)
    user=models.ForeignKey(Profile,null=True)
    car=models.ForeignKey(Car,null=True)


class Passenger(models.Model):
    name=models.CharField(max_length=40)
    national_id=models.CharField(max_length=40)
    Reviews=models.CharField(max_length=40,blank=True)
    where_are_you=models.ForeignKey(Venue,null=True)
    user=models.ForeignKey(Profile,null=True)
    Phone_number=models.CharField(max_length=40,null=True)

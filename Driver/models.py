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
we create a driver model to save information of the driver and the car
'''
class Driver(models.Model):
    start=models.CharField(max_length=40)
    destination=models.CharField(max_length=30)
'''
we create a car model to save information about the car as users may have prefrences
'''
class Car(models.Model):
    car_brand=models.CharField(max_length=30)
    Number_plate=models.CharField(max_length=40)
    seats_available=models.IntegerField(max_length=40)

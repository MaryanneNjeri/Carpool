from django import forms
from .models import Profile,Driver,Car,Venue,Passenger
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
'''
we create a signup form that as the user is signing up they also create a profile
'''

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username=forms.CharField(max_length=30, required=False, help_text='Optional.')
    sex = forms.ChoiceField(choices=(('Male','Male'),('Female','Female')))
    user_type = forms.ChoiceField(choices=(('Driver', 'Driver'), ('Passenger', 'Passenger')))
    profile_image=forms.ImageField()
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','profile_image','sex','user_type' ,'password1', 'password2')
class DriverForm(forms.ModelForm):
    class Meta:
        model=Driver
        fields=['start','destination']
class CarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields=['car_brand','seats_available','Number_plate']
class VenueForm(forms.ModelForm):
    class Meta:
        model=Venue
        fields=['name','latitude','longitude']
class PassForm(forms.ModelForm):
    class Meta:
        model=Passenger
        fields=['national_id','Phone_number','where_are_you']
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Passenger
        fields=['Reviews']

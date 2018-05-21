from django import forms
from .models import Profile
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

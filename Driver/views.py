from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm,DriverForm,CarForm,VenueForm,PassForm,ReviewForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Car,Driver,Venue,Passenger
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.core.serializers import serialize
import json
import requests

# Create your views here.
def signup(request):

    if request.method == 'POST':
        form=SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.username=form.cleaned_data.get('username')
            user.profile.profile_image=form.cleaned_data.get('profile_image')
            user.profile.sex=form.cleaned_data.get('sex')
            user.profile.user_type=form.cleaned_data.get('user_type')
            user.save()
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=user.username,password=raw_password)
            return redirect (landing)
            login(request, user)
            return redirect (landing)

    else:
        form=SignUpForm()
    return render (request,'signup.html',{"form":form})
@login_required(login_url='/accounts/login')
def landing (request):
    title='welcome driver'
    profile=Profile.objects.get(user=request.user)
    return render (request,'Driver/landing.html',{"title":title,"profile":profile})


'''
django has framework that transaltes django models into other formats, by specifying the formart and what should be serialized
'''

def profile(request,profile_id):
    current_profile=Profile.objects.get(id=profile_id)
    venue_set=Venue.objects.filter(user=current_profile)
    trips=Driver.objects.filter(user=current_profile)
    passengers=Passenger.objects.filter(where_are_you=venue_set)
    form=VenueForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            venue=form.save(commit=False)
            venue.user=current_profile
            venue.save()
            return redirect (profile,request.user.id)
    else:
        form=VenueForm()
    spots=list(Venue.objects.filter(user=current_profile))
    coords = {"1":1,"2":2}
    coords_json=json.dumps(coords,cls=DjangoJSONEncoder)
    spots_json=serializers.serialize('json',spots,cls=DjangoJSONEncoder)
    return render(request,'Driver/profile.html',{"current_profile":current_profile,"trips":trips,"form":form,"coords_json":coords_json,"spots_json":spots_json,"passengers":passengers})

'''
we create a view function car that saves information abouth the car
'''
def car(request,profile_id):
    current_profile=Profile.objects.get(id=profile_id)
    form=CarForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect (profile,request.user.id)
    else:
        form=CarForm()
    return render(request,'Driver/car.html',{"form":form,"current_profile":current_profile})
'''
a view function that saves the trip based on the car that the current driver has saved
thus a driver is only allowed to put in one car
'''
def trip(request,profile_id):
    current_profile=Profile.objects.get(id=profile_id)
    car_instance=Car.objects.get(id=profile_id)

    if request.method == 'POST':
        form=DriverForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                driver=form.save(commit=False)
                driver.user=current_profile
                driver.car=car_instance
                driver.save()
                return redirect(profile,request.user.id)
        else:
            form=DriverForm()
        if form.is_valid():
            driver=form.save(commit=False)
            driver.user=current_profile
            driver.car=car_instance
            driver.save()
            return redirect(profile,request.user.id)
    else:
        form=DriverForm()
    return render(request,'Driver/trip.html',{"form":form,"current_profile":current_profile})
'''
A view function that displays the passengers profile
'''
def passenger(request,profile_id):
    current_profile=Profile.objects.get(id=profile_id)


    return render(request,'Driver/passenger.html',{"current_profile":current_profile})
'''
a view function that displays the search results for the location
'''
def search_location(request):
    search_term=request.GET.get("location")
    searched_location=Venue.search(search_term)
    return render (request,'Driver/search.html',{"searched_location":searched_location})
'''
a view function that displays the pick up point then directions to that point
'''
def location_point(request,location_id):

    spots=list(Venue.objects.filter(id=location_id))
    coords = {"1":1,"2":2}
    coords_json=json.dumps(coords,cls=DjangoJSONEncoder)
    spots_json=serializers.serialize('json',spots,cls=DjangoJSONEncoder)
    return render (request,'Driver/location.html',{"coords_json":coords_json,"spots_json":spots_json})
'''
a view function that enables the passenger to book a trip

'''
def book(request):

    booking=Profile.objects.get(id=request.user.id)

    if request.method == 'POST':
        form=PassForm(request.POST)
        if form.is_valid():
            passenge=form.save(commit=False)
            passenge.name=request.user.username
            passenge.user=booking
            passenge.save()
            return redirect(passenger,request.user.id)
    else:
        form=PassForm()
    return render (request,'Driver/book.html',{"form":form})
'''
a view function that allows the driver to review the passenger
'''
def review(request,passenger_id):
    current_passenger=Passenger.objects.get(id=passenger_id)
    if request.method == 'POST':
        form=ReviewForm(request.POST,instance=current_passenger)
        if form.is_valid():
            form.save()
            return redirect(passenger,request.user.id)
    else:
        form=PassForm()

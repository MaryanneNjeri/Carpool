from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm,DriverForm,CarForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Car,Driver
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
            return(landing)
            login(request, user)

    else:
        form=SignUpForm()
    return render (request,'signup.html',{"form":form})
@login_required(login_url='/accounts/login')
def landing (request):
    title='welcome driver'
    profile=Profile.objects.get(user=request.user)
    return render (request,'Driver/landing.html',{"title":title,"profile":profile})

def profile(request,profile_id):
    current_profile=Profile.objects.get(id=profile_id)
    trips=Driver.objects.get(id=profile_id)
    return render(request,'Driver/profile.html',{"current_profile":current_profile,"trips":trips})
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
def trip(request,profile_id):
    current_profile=Profile.objects.get(id=profile_id)
    car_instance=Car.objects.get(id=profile_id)
    form=DriverForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            driver=form.save(commit=False)
            driver.profile=request.user
            driver.car=car_instance
            driver.save()
            return redirect(profile,request.user.id)
    else:
        form=DriverForm()
    return render(request,'Driver/trip.html',{"form":form,"current_profile":current_profile})

from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Profile
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
    return render(request,'Driver/profile.html',{"current_profile":current_profile})

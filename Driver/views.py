from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm

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
            login(request, user)
        else:
            form=SignUpForm()
        return render(request,'signup.html'.{"form":form})    
def landing (request):
    title='welcome driver'
    return render (request,'Driver/landing.html',{"title":title})

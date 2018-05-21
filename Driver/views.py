from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def landing (request):
    title='welcome driver'
    return render (request,'Driver/landing.html',{"title":title})

from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def home1(request):
    return render(request,'mysite/contact.html',{})

def home(request):
    return render(request,'mysite/home.html',{})
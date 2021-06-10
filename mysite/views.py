from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,'mysite/home.html',{})

def contacts(request):
    return render(request,'mysite/contact.html',{})
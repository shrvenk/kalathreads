from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,'mysite/home.html',{})

def contact(request):
    return render(request,'mysite/contact.html',{})
from django.shortcuts import render,get_object_or_404,redirect
from .models import ombre_detail
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic import View
from django.template.context_processors import csrf
from django.urls import reverse 

# Create your views here.
def contact(request):
    return render(request,'mysite/contact.html',{})

def home(request):
    return render(request,'mysite/home.html',{})

def page(request):
    products = ombre_detail.objects.all()
    return render(request,'mysite/page.html',{'products':products})

def frame(request):
    return render(request,'mysite/frame.html',{})
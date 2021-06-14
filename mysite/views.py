from django.shortcuts import render,get_object_or_404,redirect
# from .models import Images, detail
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

# def ombre(request):
#     products = detail.objects.filter(cat="ombre")
#     return render(request,'mysite/page.html',{'products':products})

# def plain(request):
#     products = detail.objects.filter(cat="plain")
#     return render(request,'mysite/page.html',{'products':products})

# def halfandhalf(request):
#     products = detail.objects.filter(cat="lfandhalf")
#     return render(request,'mysite/page.html',{'products':products})

# def shibori(request):
#     products = detail.objects.filter(cat="shibori")
#     return render(request,'mysite/page.html',{'products':products})

# def bandhani(request):
#     products = detail.objects.filter(cat="bandhani")
#     return render(request,'mysite/page.html',{'products':products})

# def dupatta(request):
#     products = detail.objects.filter(cat="dupatta")
#     return render(request,'mysite/page.html',{'products':products})

# def kurti(request):
#     products = detail.objects.filter(cat="kurti")
#     return render(request,'mysite/page.html',{'products':products})

# def others(request):
#     products = detail.objects.filter(cat="others")
#     return render(request,'mysite/page.html',{'products':products})

# def frame(request,idi):
#     det =get_object_or_404(detail,idi=idi)
#     pic = Images.objects.filter(idi=idi)
#     return render(request,'mysite/frame.html',{'product':det,'pic':pic})
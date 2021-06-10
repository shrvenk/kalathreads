from django.urls import path
from . import views

app_name='mysite'

urlpatterns = [
    path('',views.home,name='home'),
    path('contacts/',views.contacts,name="contact_us")
]
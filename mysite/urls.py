from django.urls import path
from . import views

urlpatterns = [
    # path('',views.cnt,name='cnt'),
    path('contact/',views.contact,name='contact')
]
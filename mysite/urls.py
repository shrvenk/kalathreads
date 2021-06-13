from django.urls import path
from . import views

urlpatterns = [
    path('cnt/',views.home,name='home'),
    path('',views.cnt,name='cnt'),
]
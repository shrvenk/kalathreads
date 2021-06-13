from django.urls import path
from . import views

urlpatterns = [
    # path('',views.cnt,name='cnt'),
    path('cnt/',views.home1,name='home')
]
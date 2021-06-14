from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    # path('ombre/',views.ombre,name='ombre'),
    # path('plain/',views.plain,name='plain'),
    # path('halfandhalf/',views.halfandhalf,name='halfandhalf'),
    # path('shibori/',views.shibori,name='shibori'),
    # path('bandhani/',views.bandhani,name='bandhani'),
    # path('dupatta/',views.dupatta,name='dupatta'),
    # path('kurti/',views.kurti,name='kurti'),
    # path('others/',views.others,name='others'),
    # path('frame/<str:idi>/',views.frame,name='frame')
]
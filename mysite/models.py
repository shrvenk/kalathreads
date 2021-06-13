from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class ombre_detail(models.Model):
    name = models.CharField(max_length=100)
    idi = models.CharField(max_length=100,default='nill')
    img = models.ImageField(null=True)
    details = models.TextField(max_length=10000,null=True)
    price = models.IntegerField()

class Images(models.Model):
    idi = models.CharField(max_length=100,default='nil') 
    img = models.ImageField()
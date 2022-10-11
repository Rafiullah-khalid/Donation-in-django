from statistics import mode
from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=30)
    cantact=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    email=models.EmailField(max_length=40)
    # category

class Donar(models.Model):
    name=models.CharField(max_length=30)
    cantact=models.CharField(max_length=30,null=True)
    address=models.CharField(max_length=30,null=True)
    Email=models.EmailField(max_length=40)
    

class Reciver(models.Model):
    name=models.CharField(max_length=30)
    f_name=models.CharField(max_length=30)
    taskera=models.CharField(max_length=40)
    cantact=models.CharField(max_length=30,null=True)
    address=models.CharField(max_length=30,null=True)

class Address(models.Model):
    country=models.CharField(max_length=40)
    city=models.CharField(max_length=40)
    distric=models.CharField(max_length=40)

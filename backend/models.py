from django.db import models
from user.models import Donar
# from django.contrib.auth.models import User
# from backend.models import Category 
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=30)
    # Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    # category = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
    quantity=models.CharField(max_length=30,null=True)
    Donar_id=models.ForeignKey(Donar,on_delete=models.CASCADE,null=True)
    receving_date=models.DateField


class Category(models.Model):
    name=models.CharField(max_length=30)



from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from .models import Donar, Employee,Reciver
from .serliazer import DonarSerializer, EmployeeSerializer,ReciverSerializer
# Create your views here.

class DonarViewSet(ListCreateAPIView):
    queryset=Donar.objects.all()
    serializer_class=DonarSerializer


class ReciverViewSet(ListCreateAPIView):
    queryset=Reciver.objects.all()
    serializer_class=ReciverSerializer

class EmployeeViewSet(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
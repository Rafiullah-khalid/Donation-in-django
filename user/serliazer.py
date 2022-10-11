from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from.models import Donar, Employee,Reciver


class DonarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donar
        fields="__all__"

class ReciverSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reciver
        fields="__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"        
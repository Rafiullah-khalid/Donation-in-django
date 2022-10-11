from django.urls import path

from .views import *

urlpatterns = [
    path("donar/", DonarViewSet.as_view()),
    path("reciver/", ReciverViewSet.as_view()),
    path("employee/", EmployeeViewSet.as_view())


]

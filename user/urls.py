from django.urls import path

from .views import *

urlpatterns = [
    path("donar/", DonarViewSet.as_view()),
    path("Donar-detial/<int:pk>", DonarDetial.as_view()),
    path("reciver/", ReciverViewSet.as_view()),
    path("reciver-detial/<int:pk>",ReciverDetail.as_view()),
    path("employee/", EmployeeViewSet.as_view()),
    path("employee-detial/<int:pk>",EmployeeDetail.as_view()),

]

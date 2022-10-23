from django.urls import path
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


from Donation import views

from .views import *

urlpatterns = [
    path("product/", ProductViewSet.as_view()),
    path("product/<int:pk>", ProductUpdate.as_view()),
    
    # path("category/", CategoryViewSet.as_view())
    # path("ap",views.apioverview,name="apiapp")
    # path("product-view/",Proview,name="productview"),
    # path('product-search/<str:pk>',Prosearch,name="product search"),
    # path('product-create/',Procreate,name="product create"),
    # path('product-update/<str:pk>',Proupdate,name="product update"),





]



from django.contrib import admin
from django.urls import path
from django.urls import path, include 
from backend.urls import *
from user.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include("backend.urls")),
    path('category/', include("backend.urls")),
    path('Donar/', include("user.urls")),
    path('Reciver/', include("user.urls")),
    path('Employee/', include("user.urls")),
    # Report=?
    





    # path('product/', admin.site.urls),


]

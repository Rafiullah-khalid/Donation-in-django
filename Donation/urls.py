from django.contrib import admin
from django.urls import path
from django.urls import path, include 
from backend.urls import *
from user.urls import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("backend.urls")),
    # path('api/', include("backend.urls")),
    path('api/', include("user.urls")),
    # path('api/', include("user.urls")),
    # path('api/', include("user.urls")),
    # path('ap/', include("backend.urls")),

    # Report=?
    





    # path('product/', admin.site.urls),


]

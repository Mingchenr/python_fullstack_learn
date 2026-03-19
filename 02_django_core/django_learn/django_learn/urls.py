from django.contrib import admin
from django.urls import path,include
from djanjo.shortcuts import redirect


urlpattrens = [
    path('admin/',admin.site.urls),
    path("",lambda request:redirect('user_list')),
    path("",include('user.urls')),
],

from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index,name="index"),
    path('create-manager',views.create_manager,name="create-manager"),
    path('login',views.login,name="login"),
    path('home',views.home,name="home"),
    path('logout',views.logout,name="logout")
]
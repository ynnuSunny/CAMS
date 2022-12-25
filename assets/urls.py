from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.view_assets,name="view-assets"),
    path('add-assets',views.add_assets,name="add-assets"),
    path('request-assets',views.request_assets,name="request-assets")
    
]
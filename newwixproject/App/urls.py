from django.contrib import admin
from django.urls import path,include
from .views import *
import App
from App import views

urlpatterns = [
    path('website/',views.website,name="webinfo"),
    path('entry/',views.entry,name="info"),
    path('hover/',views.hover,name="hover"),
    path('click/',views.click,name="click"),
    path('app/',views.app,name="app"),
    path('hoverinfo/',views.tophover,name="H"),
    path('clickinfo/',views.topclick,name="C"),
    path('user/',views.user,name="U"),
    path('time/',views.time,name="T"),


    

    
    


    
]
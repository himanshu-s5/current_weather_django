from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('home/weather/', views.weather, name='weather'),
    path('home/global/', views.global_w, name='global_w'),
    path('home/pop_n/', views.pop_n, name='pop'),
    path('home/forecast/', views.forecast, name='forcast'),
    path('index/', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('contactus/', views.contactus, name='contactus'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('register/', views.register, name='register'),
    path('login_page/', views.login_page, name='login_page'),
    path('log_out/', views.log_out, name='log_out'),
    path('bmi/', views.bmi, name='BMI_calculate'),
]

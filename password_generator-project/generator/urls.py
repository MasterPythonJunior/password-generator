from django.contrib import admin
from django.urls import path, include
from generator import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generated-password/', views.password, name='password'),
    path('about-site/', views.about, name='about'),
]
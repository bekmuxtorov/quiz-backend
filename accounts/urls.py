from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('login/', views.LoginView, name='login'),
    path('register', views.RegisterView, name='register'),
    path('', views.HomeView, name="home"),
    path('admin/', views.AdminView, name='admin'),
    path('student', views.StudentView, name='students'),

]
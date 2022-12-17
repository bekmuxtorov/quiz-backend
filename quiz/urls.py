from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExamsView, name='home'),
    path('exams/<int:pk>/', views.ExamsDetailView, name='exams_items'),
]

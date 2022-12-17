from django.urls import path
from . import views

urlpatterns = [
    path('exams/', views.ExamsApiView.as_view()),
    path('quiz/', views.QuizApiView.as_view())
]

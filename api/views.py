from rest_framework import generics
from quiz import models
from . import serializers

# Create your views here.


class ExamsApiView(generics.RetrieveAPIView):
    queryset = models.Exams.objects.all()
    serializer_class = serializers.ExamsSerailizer


class QuizApiView(generics.ListAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizSerailizer

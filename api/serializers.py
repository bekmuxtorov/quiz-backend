from rest_framework import serializers
from quiz import models


class ExamsSerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.Exams
        fields = ('name', 'science_name')


class QuizSerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = ('exam', 'question', 'answer_a',
                  'answer_b', 'answer_c', 'answer_d')

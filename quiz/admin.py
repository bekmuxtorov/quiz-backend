from django.contrib import admin
from . import models


class ExamsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'science_name']


class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_question', 'exam', 'answer']


admin.site.register(models.Exams, ExamsAdmin)
admin.site.register(models.Quiz, QuizAdmin)

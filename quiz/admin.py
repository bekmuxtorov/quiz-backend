from django.contrib import admin
from . import models


class ExamsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'science_name',
                    'time_limit', 'questions_count', 'author']


class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_question', 'exam', 'answer']


class QuizExcelAdmin(admin.ModelAdmin):
    list_display = ['id', 'exam', 'file']


admin.site.register(models.Exams, ExamsAdmin)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.QuizExcel, QuizExcelAdmin)

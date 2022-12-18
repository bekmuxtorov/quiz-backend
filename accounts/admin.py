from django.contrib import admin
from . import models
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name']


class ResultsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'exam', 'correct', 'wrong', 'time_out']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Results, ResultsAdmin)

from django.contrib import admin
from . import models
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']


class ResultsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'exam', 'result']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Results, ResultsAdmin)

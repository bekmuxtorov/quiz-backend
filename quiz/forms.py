from django import forms
from . import models


class UploadFileForm(forms.Form):
    class Meta:
        models = models.QuizExcel
        fields = ['exam', 'file']

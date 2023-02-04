from django import forms
from . import models


class UploadFileForm(forms.Form):
    class Meta:
        models = models.QuizExcel
        fields = ['exam', 'file']


class ExamForm(forms.ModelForm):
    class Meta:
        models = models.Exams
        fields = [
            "name", "science_name",
            "time_limit", "questions_count"
        ]
        widgets = {
            "name": forms.TextInput(attrs={'class': "form-control form-control-sm"}),
            "science_name": forms.TextInput(attrs={'class': "form-control form-control-sm"}),
            "time_limit": forms.TextInput(attrs={'class': "form-control form-control-sm"}),
            "questions_count": forms.TextInput(attrs={'class': "form-control form-control-sm"}),
        }

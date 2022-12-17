from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control"
            }
        )
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = models.User
        fields = (
            'name', 'surname', 'username',
            'password1', 'password2'
        )

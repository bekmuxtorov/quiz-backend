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
                'class': "form-control",
                'id': 'floatingInput'
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'firstName'
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'lastName'
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control ',
                'id': 'password1'
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'password2'
            }
        )
    )

    class Meta:
        model = models.User
        fields = (
            'first_name', 'last_name', 'username',
            'password1', 'password2'
        )

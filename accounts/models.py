from django.db import models
from django.contrib.auth.models import AbstractUser
from quiz.models import Exams
# Create your models here.


class User(AbstractUser):
    name = models.CharField(
        max_length=50,
        verbose_name='Ism'
    )

    is_admin = models.BooleanField(
        'Is admin',
        default=False
    )

    is_student = models.BooleanField(
        'Is student',
        default=True
    )


class Results(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Foydalanuvchi'
    )

    exam = models.ForeignKey(
        to=Exams,
        on_delete=models.CASCADE,
        verbose_name='Imtihon nomi'
    )

    result = models.DecimalField(
        decimal_places=2,
        verbose_name='Natija',
        max_digits=10
    )


    def __str__(self):
        return f"{self.user} || {self.exam}"

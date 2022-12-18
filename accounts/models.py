from django.db import models
from django.contrib.auth.models import AbstractUser
from quiz.models import Exams
# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(
        max_length=50,
        verbose_name='Ism'
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name='Familiya'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Kiritilgan vaqt'
    )

    image = models.ImageField(
        verbose_name='Foydalanuvchi rasmi',
        null=True,
        blank=True
    )

    bio = models.CharField(
        max_length=150,
        verbose_name='Bio',
        null=True,
        blank=True
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

    correct = models.IntegerField(
        verbose_name='To\'g\'i javob'
    )

    wrong = models.IntegerField(
        verbose_name='No\to\'g\'i javob'
    )

    time_out = models.IntegerField(
        verbose_name='Vaqt'
    )

    def __str__(self):
        return f"{self.user} || {self.exam}"

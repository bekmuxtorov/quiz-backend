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

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Temporary_user(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='Vaqtinchalik foydalanuvchi ismi',
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name='Vaqtinchalik foydalanuvchi familiyasi',
        blank=True,
        null=True
    )

    exam_name = models.ForeignKey(
        to=Exams,
        on_delete=models.CASCADE,
        verbose_name='Imtihon nomi'
    )

    correct = models.IntegerField(
        verbose_name="To'g'ri javob",
        default=0
    )

    wrong = models.IntegerField(
        verbose_name="Noto'gri javob",
        default=0
    )

    time_out = models.CharField(
        max_length=120,
        verbose_name="Vaqt",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"V. {self.first_name} {self.last_name}"


class Results(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        default=0,
        verbose_name='Foydalanuvchi'
    )

    exam = models.ForeignKey(
        to=Exams,
        on_delete=models.CASCADE,
        verbose_name='Imtihon nomi'
    )

    correct = models.IntegerField(
        verbose_name='To\'g\'i javob',
        default=0
    )

    wrong = models.IntegerField(
        verbose_name='Noto\'g\'i javob',
        default=0
    )

    time_out = models.CharField(
        max_length=120,
        verbose_name='Vaqt',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user} || {self.exam}"

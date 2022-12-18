# Generated by Django 4.1.3 on 2022-12-18 08:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_exams_quiz_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='exams',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Yaratilgan vaqt'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exams',
            name='questions_count',
            field=models.IntegerField(default=20, verbose_name="O'quvchiga chiquvchi testlar soni(ta)"),
        ),
        migrations.AddField(
            model_name='exams',
            name='time_limit',
            field=models.IntegerField(default=1, verbose_name='Har bir test uchun ajratilgan vaqt(minut)'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

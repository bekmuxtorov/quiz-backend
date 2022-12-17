# Generated by Django 4.1.3 on 2022-12-05 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Savol')),
                ('answer_a', models.CharField(max_length=200, verbose_name='A javob')),
                ('answer_b', models.CharField(max_length=200, verbose_name='B javob')),
                ('answer_c', models.CharField(max_length=200, verbose_name='C javob')),
                ('answer_d', models.CharField(max_length=200, verbose_name='D javob')),
                ('answer', models.CharField(choices=[('answer_a', 'A javob'), ('answer_b', 'B javob'), ('answer_c', 'C javob'), ('answer_d', 'D javob')], default='answer_c', max_length=10, verbose_name='Javob')),
            ],
        ),
    ]

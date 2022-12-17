from django.db import models

ANSWERS = (
    ('answer_a', 'A javob'),
    ('answer_b', 'B javob'),
    ('answer_c', 'C javob'),
    ('answer_d', 'D javob'),
)


class Exams(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=('Imtihon nomi')
    )

    science_name = models.CharField(
        max_length=50,
        verbose_name=('Fan nomi')
    )

    def __str__(self):
        return f"{self.name} || {self.science_name}"


class Quiz(models.Model):
    exam = models.ForeignKey(
        to=Exams,
        on_delete=models.CASCADE,
        verbose_name=('Imtihon')
    )

    question = models.TextField(
        verbose_name=('Savol')
    )

    answer_a = models.CharField(
        max_length=200,
        verbose_name=('A javob')
    )

    answer_b = models.CharField(
        max_length=200,
        verbose_name=('B javob')
    )

    answer_c = models.CharField(
        max_length=200,
        verbose_name=('C javob')
    )

    answer_d = models.CharField(
        max_length=200,
        verbose_name=('D javob')
    )

    answer = models.CharField(
        max_length=10,
        choices=ANSWERS,
        default='answer_c',
        verbose_name=('Javob')
    )

    def __str__(self):
        return f"{self.exam} || {(self.question)[:100]}"

    def get_question(self):
        return (self.question)[:100]

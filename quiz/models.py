from django.db import models
from django.contrib.auth.models import User

ANSWERS = (
    ('answer_a', 'A javob'),
    ('answer_b', 'B javob'),
    ('answer_c', 'C javob'),
    ('answer_d', 'D javob'),
)


class Exams(models.Model):
    author = models.CharField(
        max_length=100,
        verbose_name="Imtihon egasi"
    )

    name = models.CharField(
        max_length=50,
        verbose_name=('Imtihon nomi')
    )

    science_name = models.CharField(
        max_length=50,
        verbose_name=('Fan nomi')
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Yaratilgan vaqt'
    )

    time_limit = models.IntegerField(
        verbose_name='Har bir test uchun ajratilgan vaqt(minut)',
        default=1
    )

    questions_count = models.IntegerField(
        default=20,
        verbose_name='O\'quvchiga chiquvchi testlar soni(ta)'
    )

    status = models.CharField(
        max_length=20,
        choices=(
            ("open", "Barcha uchun ochiq"),
            ("close", "Barcha uchun yopiq")
        ),
        default="open"
    )

    def __str__(self):
        return f"{self.name} || {self.science_name}"

    def get_all_time(self):
        return self.time_limit * self.questions_count


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

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.exam} || {(self.question)[:100]}"

    def get_question(self):
        return (self.question)[:100]


def user_directory_path(exam, filename):
    exam = f"{exam}".replace(' ', '_').replace('||', '')
    return 'excelfiles/{0}/{1}'.format(exam, filename)


class QuizExcel(models.Model):
    exam = models.ForeignKey(
        to=Exams,
        verbose_name='Imtihon nomi',
        on_delete=models.CASCADE
    )

    file = models.FileField(
        upload_to=user_directory_path,
        verbose_name='Fayl'
    )

    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Qo\'shilgan vaqt:'
    )

    def __str__(self):
        return f"file {self.exam}"

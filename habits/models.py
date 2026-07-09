from django.db import models
from django.conf import settings


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="habits",
        related_query_name="habit",
    )

    place = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Место',
        help_text='Введите место привычки',
    )

    time = models.TimeField(
        verbose_name="Время привычки",
        help_text="Введите время привычки",
    )

    action = models.TextField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name="Действие",
        help_text="Опишите действие привычки",
    )

    is_pleasant = models.BooleanField(
        default=False,
        verbose_name="Приятная привычка",
        help_text="Опишите приятную привычку",
    )

    linked_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
        help_text="Опишите связанную с привычку с приятной",
        )

    periodicity = models.IntegerField(
        default=1,
        null=True,
        blank=True,
        verbose_name="Периодичность",
        help_text="Введите интервал между привычками",
    )

    reward = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Вознаграждение",
        help_text="Опишите вознаграждение",
    )

    completion_time = models.IntegerField(
        default=120,
        null=True,
        blank=True,
        verbose_name="Время выполнения",
        help_text="Введите время выполнения привычки",
    )

    is_public = models.BooleanField(
        default=False,
    )


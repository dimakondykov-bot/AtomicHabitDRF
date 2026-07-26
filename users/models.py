from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = None
    username = None
    email = models.EmailField(max_length=255, unique=True)

    telegram_chat_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Telegram Chat ID",
        help_text="Введите  ID  чата в телеграмм",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

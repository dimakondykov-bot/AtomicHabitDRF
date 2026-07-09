from celery import shared_task
from habits.models import Habit
from django.conf import settings
import requests
from django.utils import timezone
from datetime import datetime


@shared_task
def send_telegram_task():
    now = timezone.now()
    habits = Habit.objects.filter(
        time__hour=now.hour,
        time__minute=now.minute
    )
    token_tg = settings.TELEGRAM_TOKEN_TG
    for habit in habits:
        if habit.user.telegram_chat_id:
            chat_id = habit.user.telegram_chat_id
            text = f"Напоминание! Пора сделать {habit.action} в {habit.place}."
            url = f"https://api.telegram.org/bot{token_tg}/sendMessage"
            data = {
            "chat_id": chat_id,
            "text": text,
            }

            requests.post(url, data=data)
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

from habits.models import Habit

User = get_user_model()


class HabitsTestCase(APITestCase):

    def setUp(self):
        # Создаем пользователя
        self.user = User(email="test@test")
        self.user.set_password("testpassword123")
        self.user.save()

        # Авторизация пользователя
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        # Генерируем правильный url

        url = reverse("habits-list")

        data = {
            "place": "Парк",
            "time": "08:00:00",
            "action": "Бегать",
            "completion_time": 60,
            "periodicity": 1,
        }

        # POST-запрос к API
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)

    def test_create_habit_validation_time_error(self):
        url = reverse("habits-list")

        data = {
            "place": "Парк",
            "time": "08:00:00",
            "action": "Бегать",
            "completion_time": 150,
            "periodicity": 1,
        }

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Habit.objects.count(), 0)

    def test_update_habit_permission_error(self):

        habit = Habit.objects.create(
            user=self.user,
            place="Дом",
            time="09:00:00",
            action="Отжимания",
            completion_time=30,
            periodicity=1,
        )

        url = reverse("habits-detail", kwargs={"pk": habit.pk})

        another_user = User(email="hacker@user.com")
        another_user.set_password("hackerpass123")
        another_user.save()

        self.client.force_authenticate(user=another_user)

        data = {"action": "Ничего не делать"}
        response = self.client.patch(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        habit.refresh_from_db()
        self.assertEqual(habit.action, "Отжимания")

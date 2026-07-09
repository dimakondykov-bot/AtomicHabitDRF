from django.urls import path, include
from rest_framework import routers
from habits.views import HabitViewSet, PublicHabitsListView


router = routers.DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habits')


urlpatterns = [
    path('', include(router.urls)),
    path('public/', PublicHabitsListView.as_view(), name='public-habits'),
]


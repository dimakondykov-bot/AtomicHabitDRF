from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.serializers import HabitSerializer
from habits.paginators import PageNumberPagination, HabitPagination
from habits.permissions import IsOwnerOrReadOnly


class HabitViewSet(viewsets.ModelViewSet):
    """CRUD для пользователя"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PublicHabitsListView(generics.ListAPIView):
    """Список публичных привычек"""
    permission_classes = [IsAuthenticated]
    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


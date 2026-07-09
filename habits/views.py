from rest_framework import viewsets, generics, request
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from habits.models import Habit
from habits.serializers import HabitSerializer
from habits.paginators import PageNumberPagination, HabitPagination


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and obj.is_public:
            return True
        return obj.user == request.user

class HabitViewSet(viewsets.ModelViewSet):
    """CRUD для пользователя"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
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


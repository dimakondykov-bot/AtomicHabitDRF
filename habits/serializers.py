from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, attrs):
        reward = attrs.get("reward")
        linked_habit = attrs.get("linked_habit")

        if reward and linked_habit:
            raise serializers.ValidationError("Нельзя одновременно указывать вознаграждение и связанную привычку!")

        if linked_habit and not linked_habit.is_pleasant:
            raise serializers.ValidationError( "В связанные привычки можно добавлять только приятные привычки!")

        completion_time = attrs.get("completion_time")
        if completion_time and completion_time > 120:
            raise serializers.ValidationError("Время выполнения привычки не может превышать 120 секунд!")

        is_pleasant = attrs.get("is_pleasant")
        if is_pleasant and (reward or linked_habit):
            raise serializers.ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки!")

        periodicity = attrs.get("periodicity")
        if periodicity and periodicity > 7:
            raise serializers.ValidationError("Периодичность не может быть больше 7 дней. Привычку нужно выполнять хотя бы раз в неделю.")

        return attrs

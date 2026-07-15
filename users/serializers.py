import attrs
from django.contrib.auth import authenticate
from rest_framework import serializers

from users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)

        # Хеширование пароля
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {"password": {"write_only": True}}

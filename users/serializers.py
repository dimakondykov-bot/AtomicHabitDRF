import attrs
from django.contrib.auth import authenticate
from rest_framework import serializers

import users
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


class LinkTelegramSerializer(serializers.ModelSerializer):
    telegram_chat_id = serializers.IntegerField(source='tg_chat_id')

    class Meta:
        model = User
        fields = ['telegram_chat_id']
from rest_framework import generics, status, permissions
from users.models import User
from users.serializers import UserRegistrationSerializer


class UserRegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


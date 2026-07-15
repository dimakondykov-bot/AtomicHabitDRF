from rest_framework import generics, status, permissions
from rest_framework.response import Response

from users.models import User
from users.serializers import UserRegistrationSerializer


class UserRegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

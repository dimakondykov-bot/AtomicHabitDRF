from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from users.views import UserRegisterApiView, LinkTelegramAPIView

app_name = "users"

urlpatterns = [
    path("register/", UserRegisterApiView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("link-tg/", LinkTelegramAPIView.as_view(), name="link_telegram"),
]

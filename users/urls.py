from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (PaymentCreateAPIView, PaymentListAPIView,
                         UserCreateAPIView, UserDestroyAPIView,
                         UserListAPIView, UserRetrieveAPIView,
                         UserUpdateAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="pay_filter"),
    path(
        "users/register/",
        UserCreateAPIView.as_view(permission_classes=(AllowAny,)),
        name="user_register",
    ),
    path("users/", UserListAPIView.as_view(), name="user_list"),
    path("users/retrieve/<int:pk>", UserRetrieveAPIView.as_view(), name="user_get"),
    path("users/update/<int:pk>", UserUpdateAPIView.as_view(), name="user_update"),
    path("users/delete/<int:pk>", UserDestroyAPIView.as_view(), name="user_delete"),
    path(
        "users/login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path("users/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("payment/", PaymentCreateAPIView.as_view(), name="payment"),
]

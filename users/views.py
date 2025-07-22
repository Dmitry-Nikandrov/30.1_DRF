from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from users.models import Payment, User
from users.serializers import PaymentSerializers, UserSerializers


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializers
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ["course_payed", "lesson_payed", "payment_method"]
    ordering_fields = ["payment_date"]

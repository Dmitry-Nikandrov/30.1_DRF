from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import Payment, User
from users.permissions import IsCurrentuser, IsOwner
from users.serializers import PaymentSerializers, UserSerializers

from .services import (create_stripe_checkout_sessions, create_stripe_price,
                       create_stripe_product)


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
    permission_classes = (AllowAny,)


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = (IsCurrentuser,)


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ["course_payed", "lesson_payed", "payment_method"]
    ordering_fields = ["payment_date"]


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(owner=self.request.user)
        if payment.paid_course:
            product_name = f"{payment.paid_course.title} Course"
        else:
            product_name = "Additional Course"
        product = create_stripe_product(product_name)
        price = create_stripe_price(payment.amount, product)

        session_id, payment_link = create_stripe_checkout_sessions(price)

        payment.stripe_session_id = session_id
        payment.link = payment_link
        payment.save()

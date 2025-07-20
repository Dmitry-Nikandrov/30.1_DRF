from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = None
    email = models.EmailField(
        unique=True,
        max_length=30,
        verbose_name="Email",
        help_text="Укажите адрес электронной почты",
    )
    phone_number = models.CharField(
        max_length=30,
        verbose_name="Номер телефона",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )

    image = models.ImageField(
        upload_to="users/foto",
        verbose_name="Заставка",
        blank=True,
        null=True,
        help_text="Загрузите заставку",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

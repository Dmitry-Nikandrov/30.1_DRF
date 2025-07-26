from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):

    username = None

    first_name = models.CharField(
        max_length=30,
        verbose_name="Имя пользователя",
        help_text="Введите имя пользователя",
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name="Фамилие пользователя",
        help_text="Введите фамилие пользователя",
        blank=True,
        null=True,
    )
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


class Payment(models.Model):
    CASH = "наличный расчет"
    EMONEY = "перевод на счет"

    STATUS_IN_CHOICES = [
        (CASH, "наличный расчет"),
        (EMONEY, "перевод на счет"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    payment_date = models.DateField(verbose_name="Дата оплаты")
    lesson_payed = models.OneToOneField(
        'materials.Lesson',
        on_delete=models.CASCADE,
        related_name="lesson_payed",
        blank=True,
        null=True,
        verbose_name="оплаченный урок",
    )
    course_payed = models.OneToOneField(
        'materials.Course',
        on_delete=models.CASCADE,
        related_name="course_payed",
        blank=True,
        null=True,
        verbose_name="оплаченный курс",
    )
    payment = models.PositiveIntegerField(verbose_name="Сумма платежа")
    payment_method = models.CharField(
        max_length=50, choices=STATUS_IN_CHOICES, verbose_name="метод платежа"
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"{self.user} {self.lesson_payed if self.lesson_payed else self.course_payed}"

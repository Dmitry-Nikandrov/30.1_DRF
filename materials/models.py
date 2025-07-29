from django.db import models

from users.models import User


class Course(models.Model):
    name = models.CharField(
        max_length=30, verbose_name="Название курса", help_text="Укажите название курса"
    )
    visual = models.ImageField(
        upload_to="cours/foto",
        verbose_name="Картинка курса",
        blank=True,
        null=True,
        help_text="Загрузите картинку курса",
    )
    content = models.CharField(
        max_length=200,
        verbose_name="Содержание курса",
        help_text="Укажите содержание курса",
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Пользователь",
        help_text="Введите пользователя",
        related_name="course",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=30, verbose_name="Название урока", help_text="Укажите название урока"
    )
    visual = models.ImageField(
        upload_to="lesson/foto",
        verbose_name="Картинка урока",
        blank=True,
        null=True,
        help_text="Загрузите картинку урока",
    )
    content = models.CharField(
        max_length=200,
        verbose_name="Содержание урока",
        help_text="Укажите содержание урока",
    )

    related = models.URLField(
        max_length=300,
        verbose_name="Ссылка на материалы в сети",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Пользователь",
        help_text="Введите пользователя",
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь курса",
        help_text="Укажите пользователя курса",
        related_name="user_sub",
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс подписки",
        help_text="Курс для подписки",
    )

    def __str__(self):
        return f"Subscription for {self.user} ({self.course.name})"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

# Generated by Django 5.2.4 on 2025-07-21 18:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
        ("users", "0002_alter_user_options_remove_user_username_user_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("payment_date", models.DateField(verbose_name="Содержание урока")),
                ("payment", models.PositiveIntegerField(verbose_name="Сумма платежа")),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("cash", "наличный расчет"),
                            ("emoney", "перевод на счет"),
                        ],
                        max_length=50,
                        verbose_name="метод платежа",
                    ),
                ),
                (
                    "course_payed",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course_payed",
                        to="materials.course",
                        verbose_name="оплаченный курс",
                    ),
                ),
                (
                    "lesson_payed",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lesson_payed",
                        to="materials.lesson",
                        verbose_name="оплаченный урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платежи",
            },
        ),
    ]

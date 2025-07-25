# Generated by Django 5.2.4 on 2025-07-20 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название курса",
                        max_length=30,
                        verbose_name="Название курса",
                    ),
                ),
                (
                    "visual",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите картинку курса",
                        null=True,
                        upload_to="cours/foto",
                        verbose_name="Картинка курса",
                    ),
                ),
                (
                    "content",
                    models.CharField(
                        help_text="Укажите содержание курса",
                        max_length=200,
                        verbose_name="Содержание курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название урока",
                        max_length=30,
                        verbose_name="Название урока",
                    ),
                ),
                (
                    "visual",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите картинку урока",
                        null=True,
                        upload_to="lesson/foto",
                        verbose_name="Картинка урока",
                    ),
                ),
                (
                    "content",
                    models.CharField(
                        help_text="Укажите содержание урока",
                        max_length=200,
                        verbose_name="Содержание урока",
                    ),
                ),
                (
                    "related",
                    models.URLField(
                        blank=True,
                        default="https://my.sky.pro",
                        max_length=300,
                        null=True,
                        verbose_name="Ссылка на материалы в сети",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course",
                        to="materials.course",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]

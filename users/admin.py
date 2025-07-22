from django.contrib import admin

from materials.models import Course, Lesson
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email")


@admin.register(Lesson, Course)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "name")

from django.contrib import admin

from materials.models import Course, Lesson, Subscription
from users.models import Payment, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email", "first_name", "first_name")


@admin.register(Lesson, Course)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "name")


@admin.register(Payment)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("user", "lesson_payed", "course_payed", "payment")


@admin.register(Subscription)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("user", "course")

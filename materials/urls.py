from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonDestroyAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
)

app_name = MaterialsConfig.name
router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")

urlpatterns = [
    path("lesson/create", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lesson/", LessonListAPIView.as_view(), name="lesson_list"),
    path(
        "lesson/retrieve/<int:pk>", LessonRetrieveAPIView.as_view(), name="lesson_get"
    ),
    path("lesson/update/<int:pk>", LessonUpdateAPIView.as_view(), name="lesson_update"),
    path(
        "lesson/delete/<int:pk>", LessonDestroyAPIView.as_view(), name="lesson_delete"
    ),
] + router.urls

from rest_framework import generics, viewsets

from materials.models import Course, Lesson
from materials.serializers import CourseSerializers, LessonSerializers


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()

from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializers(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson_in_course = LessonSerializers(source="course", many=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_lesson_count(self, object):
        return object.course.all().count()

from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import UrlValidator


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidator(field="related")]


class CourseSerializers(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson_in_course = LessonSerializers(source="course", many=True)

    def get_lesson_count(self, object):
        return object.course.all().count()

    def get_lesson_count(self, object):
        def has_object_permission(self, request, view, obj):
            if obj.owner == request.user:
                return True
            return False

    class Meta:
        model = Course
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

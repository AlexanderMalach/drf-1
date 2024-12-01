from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """
    Сериализатор для модели Dog.
    """

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    """
    Сериализатор для модели Breed.
    """

    class Meta:
        model = Lesson
        fields = "__all__"

from rest_framework import serializers

from .models import Comment, Course, Lesson, Like_or_DislikeLesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like_or_DislikeLesson
        fields = '__all__'


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
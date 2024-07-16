from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Comment, Course, Lesson, User, Like_or_DislikeVideo
from .serializers import CourseSerializer, CommentSerializer, LessonSerializer, EmailSerializer, VideoLikeSerializer
from .permissions import CoursePermission, LessonPermission


class CourseAPIViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [CoursePermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ["course_name"]


class LessonAPIViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [LessonPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]


class CommentAPIViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    



class SendEmailToUserView(APIView):
    def post(self, request: Request):   
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)   

        users = User.objects.all()
        user_email = []
        for user in users:
            user_email.append(user.email)
        user_email.append("hasanboynasirdinov@gmail.com")

        send_mail(
            serializer.validated_data.get("sabject"),
            serializer.validated_data.get("message"),
            settings.EMAIL_HOST_USER,
            user_email,
            fail_silently=False,
        )
        return Response({"message":"Xabar yuborildi."})


class VideoLikesView(APIView):
    def post(self, request):
        try:
            like_or_dislike = Like_or_DislikeVideo.objects.filter(author_id=request.data.get("author"))
            for like in like_or_dislike:
                like.delete()
        except:
            pass

        serializer = VideoLikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_or_dislike = serializer.save()
        return Response(VideoLikeSerializer(like_or_dislike))
    

    
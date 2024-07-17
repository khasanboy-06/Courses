from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Rest frameworkdan chaqirilgan kutub
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import permissions

# App ning o'zidan chaqirilgan modellar
from .models import Comment, Course, Lesson, User, Like_or_DislikeLesson
from .serializers import CourseSerializer, CommentSerializer, LessonSerializer, EmailSerializer, LessonLikeSerializer
from .permissions import CoursePermission, LessonPermission

# Kurslar uchun yozilgan view
class CourseAPIViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [CoursePermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ["course_name"]
#-----------Tugashi--------------

# Darslar uchun yozilgan view
class LessonAPIViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [LessonPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]
#-----------Tugashi--------------

# Izoh uchun yozilgan view
class CommentAPIViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#-----------Tugashi--------------
    

# Emailga habar yuborish qismi
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
#---------------Tugashi-----------------

# Darsning like qismini ko'rish uchun yozilgan view
class LikeLessonView(APIView):
    def get(self, request, pk):
        like = len(Like_or_DislikeLesson.objects.filter(like_or_dislike=True, lesson_model_id=pk))
        dislike = len(Like_or_DislikeLesson.objects.filter(like_or_dislike=True, lesson_model_id=pk))
        return Response({"like":like, "dislike":dislike})
#--------------Tugashi---------------
    
# Like bosish imkonini beruvchi view
class CreateLikeLessonView(APIView):
    def post(self, request):
        try:
            like_dislike = Like_or_DislikeLesson.objects.filter(author_id=request.data.get("author"))
            for like in like_dislike:
                like.delete()
        except:
            pass
        serializer = LessonLikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_or_dislike = serializer.save()
        return Response(LessonLikeSerializer(like_or_dislike).data)
#---------------Tugashi---------------
    
from django.contrib import admin

from .models import Comment, Lesson, Course, User, Like_or_DislikeVideo


admin.site.register([Comment, Course, Lesson, User, Like_or_DislikeVideo])
from django.contrib import admin

from .models import Comment, Lesson, Course, User, Like_or_DislikeLesson

# class CoursesAdmin(admin.ModelAdmin):
#     list_display = ("pk", "course_name", "price", "about")


admin.site.register([Comment, 
                     Course, 
                     Lesson, User, Like_or_DislikeLesson])
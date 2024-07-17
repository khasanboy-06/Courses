from django.contrib import admin

from .models import Comment, Lesson, Course, User, Like_or_DislikeLesson

# kurs modelini adminga registratsiya qilish qismi.
@admin.register(Course)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ("pk", "course_name", "price", "about")
    list_display_links = ("course_name",)
    list_filter = ("course_name",)
    search_fields = ("course_name", "about",)
    ordering = ("course_name",)
#-------------Tugashi-------------

# Darslar modelini adminga registratsiya qilish qismi.
class CommentInline(admin.StackedInline):
    model=Comment
    extra=0
class LikeInline(admin.StackedInline):
    model=Like_or_DislikeLesson
    extra=1

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "created", "course", "video")
    list_display_links = ("title",)
    list_filter = ("course",)
    search_fields = ("title", "course",)
    ordering = ("title",)
    inlines = [
        CommentInline,
        LikeInline
    ]
#--------------Tugashi-------------

# User modelini adminga registratsiya qilish qismi.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "first_name", "last_name", "email", "phone_number")
    list_display_links = ("first_name",)
    search_fields = ("first_name", "last_name", "email_address", "phone_number")
    ordering = ("first_name",)
#-------------Tugashi-------------






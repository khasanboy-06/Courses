from django.db import models
from django.core.validators import FileExtensionValidator 
from django.contrib.auth.models import AbstractUser

# User modeli
class User(AbstractUser):
    phone_number = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.first_name
#----------User modelining tugashi------------

# Kurslar modeli
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    price = models.IntegerField()
    about = models.TextField()
    
    def __str__(self) -> str:
        return self.course_name
#---------Kurslar modelining tugashi-----------

# Darslar modeli
class Lesson(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video = models.FileField(upload_to='video/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'mp3', 'AVI', 'WMV'])
    ])

    def __str__(self) -> str:
        return self.title
#--------Darslar modelining tugashi------------

# Izoh va Like modellari  
class Comment(models.Model):
    text = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class Like_or_DislikeLesson(models.Model):
    lesson_model = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    like_or_dislike = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
#-----------------Tugashi-----------------


 
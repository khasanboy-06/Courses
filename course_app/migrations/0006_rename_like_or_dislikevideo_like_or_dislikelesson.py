# Generated by Django 5.0.7 on 2024-07-16 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0005_remove_like_or_dislikevideo_video_model_lesson_video_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like_or_DislikeVideo',
            new_name='Like_or_DislikeLesson',
        ),
    ]
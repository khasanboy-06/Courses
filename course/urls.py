"""
URL configuration for course project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

from course_app.views import (LessonAPIViewSet, CommentAPIViewSet, CourseAPIViewSet, 
                               SendEmailToUserView, LikeLessonView, CreateLikeLessonView)

router = routers.SimpleRouter()
router.register('lesson', LessonAPIViewSet, basename='lesson')
router.register('comment', CommentAPIViewSet, basename='comment')
router.register('course', CourseAPIViewSet, basename='course')

# Registratsiya qismi urli
api_urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/send/email/', SendEmailToUserView.as_view()),
    path('api/v1/lesson/<int:pk>/like/', LikeLessonView.as_view()),
    path('api/v1/like/create/', CreateLikeLessonView.as_view()),

    # Router url.
    path('api/v1/', include(router.urls)),
    
    # Login va Registratsiya urls.
    path('api-auth/', include('rest_framework.urls')), 
    path('api/v1/', include(api_urlpatterns)),
     
    # Swagger urls.
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

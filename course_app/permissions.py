from rest_framework.permissions import BasePermission, SAFE_METHODS     

# Darslar uchun berilgan ruxsat va cheklovlar
class LessonPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_superuser and request.method == 'DELETE':
            return True
        return False
#---------------------------------------------------

# Kurslar uchun berilgan ruxsat va cheklovlar
class CoursePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.method in SAFE_METHODS
#-----------------------------------------------

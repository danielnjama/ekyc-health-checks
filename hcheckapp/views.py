from rest_framework import viewsets, permissions, generics, filters
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .models import ServiceHealthData
from .serializers import ServiceHealthDataSerializer
from rest_framework.permissions import IsAuthenticated

class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_staff

class healthViewSet(viewsets.ModelViewSet):
    queryset = ServiceHealthData.objects.all()
    serializer_class = ServiceHealthDataSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]
    


# class IsAdminUserOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return request.user and request.user.is_staff
 
# class healthViewSet(viewsets.ModelViewSet):
#     queryset = healthdata.objects.all()
#     serializer_class = healthdataSerializer
#     permission_classes = [IsAdminUserOrReadOnly]


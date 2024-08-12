from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import healthViewSet

router = DefaultRouter()
router.register(r'health', healthViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    
    
]

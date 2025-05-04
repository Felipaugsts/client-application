from rest_framework.routers import DefaultRouter
from .views import JobViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', JobViewSet, basename='job') 

urlpatterns = [
    path('api/', include(router.urls)),
]

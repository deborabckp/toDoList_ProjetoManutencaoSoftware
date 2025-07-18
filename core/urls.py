"""URLs da app core."""

from django.urls import path, include
from rest_framework import routers

from .views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('api/', include(router.urls)),
]

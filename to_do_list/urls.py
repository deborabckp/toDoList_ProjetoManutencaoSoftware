from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from core.views import TaskViewSet
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', core_views.home, name='home'),

    path('task/<uuid:pk>/edit/',   core_views.task_update,  name='task_update'),
    path('task/<uuid:pk>/delete/', core_views.task_delete,  name='task_delete'),

    path('task/create/', core_views.task_create, name='task_create'),

    path('login/',  auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),                    name='logout'),

    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls')), 

]

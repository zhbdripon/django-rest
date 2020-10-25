from django.urls import path, include
from rest_framework.authtoken import views
from rip_auth.views import UserViewSet, GroupViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('token-auth/', views.obtain_auth_token),
]

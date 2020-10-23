from django.urls import path, include
from rip_auth.views import api_root, UserList, UserDetail, GroupList, GroupDetail
from rest_framework.authtoken import views

urlpatterns = [
    path('',api_root),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('groups/', GroupList.as_view()),
    path('groups/<int:pk>/', GroupDetail.as_view()),
    path('token-auth/', views.obtain_auth_token),
]

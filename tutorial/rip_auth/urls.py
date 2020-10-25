from django.urls import path, include
from rip_auth.views import api_root, GroupList, GroupDetail
from rest_framework.authtoken import views

from rip_auth.views import UserViewSet

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('',api_root),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('groups/', GroupList.as_view()),
    path('groups/<int:pk>/', GroupDetail.as_view()),
    path('token-auth/', views.obtain_auth_token),
]

from django.urls import path, include
from rip_auth.views import UserList, UserDetail, GroupList, GroupDetail
from rest_framework.authtoken import views

urlpatterns = [
    path('token-auth/', views.obtain_auth_token),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('groups/', GroupList.as_view()),
    path('groups/<int:pk>/', GroupDetail.as_view()),
]

from django.urls import path, include
from snippets.views import SnippetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
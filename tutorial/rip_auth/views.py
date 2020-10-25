from django.contrib.auth.models import User, Group
from rip_auth.serializers import UserSerializer, GroupSerializer
from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import viewsets

@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class GroupList(generics.ListAPIView):
    querySet = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveAPIView):
    querySet = Group.objects.all()
    serializer_class = GroupSerializer

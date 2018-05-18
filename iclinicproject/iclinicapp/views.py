from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
#from iclinicproject.iclinicapp.serializers import UserSerializer, GroupSerializer
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer

def pagina_inicial(request):
    return render(request, 'index.html')

from iclinicapp.models import Agenda
from iclinicapp.serializers import AgendaSerializer
from django.contrib.auth.models import User
from iclinicapp.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import viewsets

#from rest_framework import permissions
#from iclinicapp.permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'agendamento': reverse('agenda-list', request=request, format=format)
    })


class AgendaViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a meeting instance.

        Status Code:
        200: Successful operation
        404: ID not found

    list:
        Return all meeting, ordered by most recently added.

    create:
        Creates a new Meeting

        Status Code:
        201: Successful operation


    delete:
        Remove an existing meeting.

        Status Code:
        204: Successful operation
        404: ID not found

    partial_update:
        Update one or more fields on an existing meeting.

    update:
        Update a meeting.

        Status Code:
        200: Successful operation
        404: ID not found
    """

    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        Return a user instance.

    list:
        Return all user, ordered by most recently added.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
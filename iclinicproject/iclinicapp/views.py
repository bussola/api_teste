from iclinicapp.models import Agenda
from iclinicapp.serializers import AgendaSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from iclinicapp.serializers import UserSerializer
from rest_framework import permissions
from iclinicapp.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework.decorators import action


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'agendamento': reverse('agenda-list', request=request, format=format)
    })


class AgendaViewSet(viewsets.ModelViewSet):
    # """
    # retrieve:
    #     Return a meeting instance.

    # list:
    #     Return all meeting, ordered by most recently added.

    # create:
    #     Creates a new Meeting

    # delete:
    #     Remove an existing meeting.

    # partial_update:
    #     Update one or more fields on an existing meeting.

    # update:
    #     Update a meeting.
    # """

    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     agenda = self.get_object()
    #     return Response(agenda.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        """
            Return a meeting instance.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
            Update one or more fields on an existing meeting.
        """
        return self.bulk_update(request, *args, **kwargs)

    # def list(self, request):
    #     queryset = User.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)
        


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        Return a user instance.

    list:
        Return all user, ordered by most recently added.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
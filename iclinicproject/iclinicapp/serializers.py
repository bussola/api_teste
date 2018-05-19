from rest_framework import serializers
from iclinicapp.models import Agenda, PROC_CHOICES
from django.contrib.auth.models import User

class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Agenda
        fields = ('url', 'id', 'owner',
        		  'data', 'hor_inicio', 'hor_final', 
                  'paciente', 'procedimento')
                  # 'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    agendamento = serializers.HyperlinkedRelatedField(many=True, view_name='agenda-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'agendamento')
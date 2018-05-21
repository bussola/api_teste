from rest_framework import serializers
from iclinicapp.models import Agenda
from django.contrib.auth.models import User
import datetime

class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Agenda
        fields = ('url', 'id', 'owner',
        		  'data', 'hora_inicio', 'hora_final', 
                  'paciente', 'procedimento')

    def create(self, validated_data):
        if validated_data['data'] <= datetime.datetime.now().date():
            raise Exception
        return Agenda.objects.create(**validated_data)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    agendamento = serializers.HyperlinkedRelatedField(many=True, view_name='agenda-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'agendamento')
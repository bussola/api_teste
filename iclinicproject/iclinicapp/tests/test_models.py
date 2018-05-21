from django.test import TestCase
from iclinicapp.models import Agenda
from django.contrib.auth.models import User
from rest_framework import serializers
import datetime
from urllib import request


global user_id 
user_id = request.user.id

class IclinicModelsTestCase(TestCase):
	def setUp(self):
		u = User.objects.create_user(username="joao", first_name='olivia')
		u.save()
		#self.user = u
		#self.user = serializers.ReadOnlyField(source='owner.username')
		user = User.objects.get(id=user_id)
		self.user = user
		Agenda.objects.create(data="2018-05-19", hora_inicio="10:10:AM", hora_final="10:10:AM", paciente="Jose", procedimento="Consulta", owner=self.user, highlighted="shero")

	def test_usuario_nao_autenticado(self):
		dados = {
			'data': '2018-05-21',
			'hora_inicio': "10:10:AM",
			'hora_final': "10:10:AM",
		   	'paciente':"Jose",
			'procedimento':'consulta',
			'owner':str(self.user.id),
			'highlighted':'shero'}
		response = self.client.post('/agendamento/', dados)
		description = response
		assert response.status_code == 403


	def test_2(self):
		a = 1
		assert a == 1
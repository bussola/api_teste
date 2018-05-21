from django.test import TestCase
from iclinicapp.models import Agenda
from django.contrib.auth.models import User
from rest_framework import serializers
import datetime
from urllib import request


class IclinicModelsTestCase(TestCase):
	def setUp(self):
		u = User.objects.create_user(username="joao", first_name='olivia')
		u.save()
		self.user = u
		#self.user = serializers.ReadOnlyField(source='owner.username')
		#user = User.objects.get(id=user_id)
		#self.user = user
		Agenda.objects.create(data="2018-05-19", hora_inicio="10:10:AM", hora_final="10:10:AM", paciente="Jose", procedimento="Consulta", owner=self.user)

	def test_data_passado(self):
		dados = {
			'data': '2018-05-30',
			'hora_inicio': "10:10:AM",
			'hora_final': "10:10:AM",
		   	'paciente':"Jose",
			'procedimento':'consulta',
			'owner':str(self.user.id),}
		response = self.client.post('/agendamento/', dados)
		assert response.status_code == 403
		#self.assertRaises(Exception, Agenda, data='2018-05-20')


	def test_2(self):
		a = 1
		assert a == 1
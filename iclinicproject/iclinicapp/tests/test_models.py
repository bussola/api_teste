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
		Agenda.objects.create(data="2018-05-30", hora_inicio="10:10:AM", hora_final="10:10:AM", paciente="Jose", procedimento="Consulta", owner=self.user)

	# def test_data_futura(self):
	# 	dados = {
	# 		'data': '2018-05-30',
	# 		'hora_inicio': "10:10:AM",
	# 		'hora_final': "10:10:AM",
	# 	   	'paciente':"Jose",
	# 		'procedimento':'consulta',
	# 		'owner':str(self.user.id),}
	# 	response = self.client.post('/agendamento/', dados)
	# 	print(response.status_code)
	# 	assert response.status_code == 200
	# 	#self.assertRaises(Exception, Agenda, data='2018-05-20')

	def test_get(self):
		response = self.client.get('/agendamento/1/')
		assert response.status_code == 200


	def test_get_all(self):
		response = self.client.get('/agendamento/')
		assert response.status_code == 200


	def test_post(self):
		dados = {
			'data': '2018-05-30',
			'hora_inicio': "10:10:AM",
			'hora_final': "10:10:AM",
			'paciente':"Jose",
			'procedimento':'consulta',
			'owner':'iclinic',}
		response = self.client.post('/agendamento/', dados, format='json')
		print(response.status_code)
		#self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		assert response.status_code == 201


	def test_delete(self):
		dados = {
			'data': '2018-05-30',
			'hora_inicio': "10:10:AM",
			'hora_final': "10:10:AM",
			'paciente':"Jose",
			'procedimento':'consulta',
			'owner':'iclinic',}
		response = self.client.post('/agendamento/', dados, format='json')
		response = self.client.delete("/agendamento/", dados, format='json')
		#assert response.status_code == 200
		self.assertEqual(response.status_code, status.HTTP_200_OK)
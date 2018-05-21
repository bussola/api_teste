from django.test import TestCase
from rest_framework.test import APITestCase

from iclinicapp.models import Agenda
from django.contrib.auth.models import User
from rest_framework import serializers
import datetime
from urllib import request


class IclinicModelsTestCase(APITestCase):
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



	#**********************  USER   **********************
	# def test_get_user(self):
	# 	response = self.client.get('/users/1/')
	# 	assert response.status_code == 200

	# def test_get_all_users(self):
	# 	response = self.client.get('/users/')
	# 	assert response.status_code == 200



	#**********************  AGENDA   **********************
	def test_post(self):
		dados = {
			'id': '100',
			'data': '2018-05-30',
			'hora_inicio': "10:10:AM",
			'hora_final': "10:10:AM",
			'paciente':"Jose",
			'procedimento':'consulta',
			'owner':'iclinic',}
		response = self.client.post('/agendamento/', dados, format='json')
		assert response.status_code == 201


	def test_get_agendamento(self):
		response = self.client.get('/agendamento/1/')
		assert response.status_code == 200


	def test_get_all(self):
		response = self.client.get('/agendamento/')
		assert response.status_code == 200


	# def test_put(self):
	# 	dados = {
	# 		'data': '2018-05-30',
	# 		'hora_inicio': "10:10:AM",
	# 		'hora_final': "10:10:AM",
	# 		'paciente':"Joao",
	# 		'procedimento':'consulta',
	# 		'owner':'iclinic',}
	# 	response = self.client.put('/agendamento/1/', dados)
	# 	assert response.status_code == 200


	def test_z_delete(self):
		dados = {
			'id': '101',
			'data': '2018-05-30',
			'hora_inicio': "10:10:AM",
			'hora_final': "10:10:AM",
			'paciente':"Jose",
			'procedimento':'consulta',
			'owner':'iclinic',}
		response = self.client.post('/agendamento/', dados, format='json')
		assert response.status_code == 201
		response = self.client.delete("/agendamento/", dados)
		assert response.status_code == 201
		#assert response.status_code == 202
		#assert response.status_code == 204
		#self.assertEqual(response.status_code, status.HTTP_200_OK)


	# def test_login(self):
	# 	response = self.client.login(username='iclinic', password='senha123')
	# 	assert response.status_code == 201
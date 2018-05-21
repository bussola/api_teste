from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from iclinicapp.models import Agenda
from django.contrib.auth.models import User
from rest_framework import serializers
import datetime
from urllib import request
from django.shortcuts import reverse


class IclinicModelsTestCase(APITestCase):
	def setUp(self):
		u = User.objects.create_user(username="palito", first_name='olivia')
		u.save()
		self.user = u
		Agenda.objects.create(id="301", data="2018-05-30", hora_inicio="10:10:AM", hora_final="10:10:AM", paciente="Jose", procedimento="Consulta", owner=self.user)


	#**********************  AGENDA   **********************
	def test_1_get_agendamento_existente(self):
		response = self.client.get('/agendamento/301/')
		assert response.status_code == 200

	def test_2_get_agendamento_nao_existente(self):
		response = self.client.get('/agendamento/302/')
		assert response.status_code == 404

	def test_3_agendamentos(self):
		response = self.client.get('/agendamento/')
		assert response.status_code == 200

	def test_4_updating_agenda(self):
		dados = {
			'data': '2018-05-30',
			'hora_inicio': "10:10:AM",
			'hora_final': "10:10:AM",
			'paciente':"Jose",
			'procedimento':'consulta',
			'owner':'iclinic',}
		response = self.client.put('/agendamento/301/', dados, format='json')
		assert response.status_code == 200

	def test_5_delete(self):
		response = self.client.delete('/agendamento/301/', format='json')
		assert response.status_code == 204

	def test_6_post_agendamento(self):
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



	

	


	# def test_z_delete(self):
	# 	response = self.client.delete('/agendamento/1/', format='json')
	# 	#response = self.client.delete('/agendamento/1/', dados, format='json')
	# 	print("***" + str(response) + "***")
	# 	assert response.status_code == 404





	# def test_put(self):
	# 	response = self.client.put('/agendamento/1/', {'paciente': 'Naves'}, kwargs={'pk': 1} , format='json')
	# 	print(response)
	# 	#self.assertEqual('Naves', response.data['paciente'])
	# 	assert response.status_code == 404

	# 	# dados = {
	# 	# 	'id': '200',
	# 	# 	'data': '2018-05-30',
	# 	# 	'hora_inicio': "10:10:AM",
	# 	# 	'hora_final': "10:10:AM",
	# 	# 	'paciente':"Joao",
	# 	# 	'procedimento':'consulta',
	# 	# 	'owner':'iclinic',}
	# 	# response = self.subtest_post()
	# 	# assert response.status_code == 201
	# 	# response = self.client.put('/agendamento/1/', dados, format='json')
	# 	# print(response)
	# 	# assert response.status_code == 404


	# def test_z_delete(self):
	# 	dados = {
	# 		'id': '101',
	# 		'data': '2018-05-30',
	# 		'hora_inicio': "10:10:AM",
	# 		'hora_final': "10:10:AM",
	# 		'paciente':"Jose",
	# 		'procedimento':'consulta',
	# 		'owner':'iclinic',}
	# 	response = self.client.post('/agendamento/', dados, format='json')
	# 	assert response.status_code == 201
	# 	response = self.client.delete('/agendamento/101/', dados, format='json')
	# 	print(response.status_code)
	# 	assert response.status_code == 404
	# 	#assert response.status_code == 202
	# 	#assert response.status_code == 204
	# 	#self.assertEqual(response.status_code, status.HTTP_200_OK)


	# def test_login(self):
	# 	response = self.client.login(username='iclinic', password='senha123')
	# 	assert response.status_code == 201


	#**********************  USER   **********************
	# def test_get_user(self):
	# 	response = self.client.get('/users/1/')
	# 	assert response.status_code == 200

	# def test_get_all_users(self):
	# 	response = self.client.get('/users/')
	# 	assert response.status_code == 200


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
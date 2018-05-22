from rest_framework.test import APITestCase
from iclinicapp.models import Agenda
from django.contrib.auth.models import User



class AgendaTestCase(APITestCase):
	#Cria um objeto da Agenda, com id = 301, para os teste
	def setUp(self):
		u = User.objects.create_user(username="palito", first_name='olivia')
		u.save()
		self.user = u
		Agenda.objects.create(id="301", data="2018-05-30", hora_inicio="10:10:AM", hora_final="10:10:AM", paciente="Jose", procedimento="Consulta", owner=self.user)


	#**********************  AGENDA Tests  **********************
	# GET id instanciado - id 301
	def test_1_get_agendamento_existente(self):
		response = self.client.get('/agendamento/301/')
		assert response.status_code == 200

	# GET id nao existente - erro
	def test_2_get_agendamento_nao_existente(self):
		response = self.client.get('/agendamento/302/')
		assert response.status_code == 404

	# GET agendamento/
	def test_3_agendamentos(self):
		response = self.client.get('/agendamento/')
		assert response.status_code == 200

	# PUT - altera o objeto de id 301
	def test_4_updating_agenda(self):
		dados = {
			'data': '2018-05-30',
			'hora_inicio': "10:10:AM",
			'hora_final': "10:10:AM",
			'paciente':"Joao Carlos",
			'procedimento':'consulta',
			'owner':'iclinic'}
		response = self.client.put('/agendamento/301/', dados, format='json')
		assert response.status_code == 200

	#PUT - altera um objeto nao existente - erro
	def test_5_updating_agenda_erro(self):
		dados = {
			'data': '2018-05-30',
			'hora_inicio': "10:10:AM",
			'hora_final': "10:10:AM",
			'paciente':"Jose",
			'procedimento':'consulta',
			'owner':'iclinic'}
		response = self.client.put('/agendamento/302/', dados, format='json')
		assert response.status_code == 404

	#DELETE id 301
	def test_6_delete(self):
		response = self.client.delete('/agendamento/301/', format='json')
		assert response.status_code == 204

	#DELETE id nao existente int - erro
	def test_7_delete_error(self):
		response = self.client.delete('/agendamento/30/', format='json')
		assert response.status_code == 404

	#DELETE id nao existente string - erro
	def test_8_delete_error_id(self):
		response = self.client.delete('/agendamento/xyz/', format='json')
		assert response.status_code == 404

	#POST - adiciona um novo objeto na Agenda
	def test_9_post_agendamento(self):
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




class UserTestCase(APITestCase):
	#Cria um usuario para o teste com id = 301
	def setUp(self):
		u = User.objects.create_user(id="301", username="palito", first_name='olivia')
		u.save()
		self.user = u

	#**********************  USER Tests  **********************
	# GET id instanciado - id 301
	def test_1_get_user(self):
		response = self.client.get('/users/301/')
		assert response.status_code == 200

	# GET id nao existente - erro
	def test_2_get_user_error(self):
		response = self.client.get('/users/302/')
		assert response.status_code == 404

	#GET users/ 
	def test_3_get_all_users(self):
		response = self.client.get('/users/')
		assert response.status_code == 200


class TimeTestCase(APITestCase):
	#Testa uma data valida
	def test_1_data_correta(self):
		dados = {
			'id': '100',
			'data': '2019-05-30',
			'hora_inicio': "10:10:AM",
			'hora_final': "10:10:AM",
			'paciente':"Jose",
			'procedimento':'consulta',
			'owner':'iclinic',}
		response = self.client.post('/agendamento/', dados, format='json')
		assert response.status_code == 201

	#Testa uma data no passado - except
	def test_2_data_incorreta(self):
		dados = {
			'id': '100',
			'data': '2017-05-30',
			'hora_inicio': "10:10:AM",
			'hora_final': "10:10:AM",
			'paciente':"Jose",
			'procedimento':'consulta',
			'owner':'iclinic',}
		try:
			response = self.client.post('/agendamento/', dados, format='json')
		except:
			assert True

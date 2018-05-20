from django.test import TestCase
from iclinicapp.models import Agenda
from django.contrib.auth.models import User
from django.contrib.auth.models import User



class AnimalTestCase(TestCase):
	def setUp(self):
		User.objects.create(name="Jose")
		user = User.objects.values('name')[0]
		#user = User.objects.get(id=user_id)
		Agenda.objects.create(data="2018-05-19", hora_inicio="10:10:AM", hora_final="10:10:AM", paciente="Jose", procedimento="Consulta", owner=user, highlighted="shero")
		#Agenda.objects.create(data="05/09/2017", hora_inicio="10:10:AM")

	def test_1(self):
		instance = Agenda.objects.values('data')[0]
		description = instance['description']
		self.assertEqual(description, '2018-05-19')

	def test_2(self):
		a = 1
		assert a == 2
from django.test import TestCase
from iclinicapp.models import Agenda

class AnimalTestCase(TestCase):
	def setUp(self):
		Agenda.objects.create(data="2018-05-19", hora_inicio="10:10:AM", hora_final="10:10:AM", paciente="Jose", procedimento="Consulta", owner="iclinic", highlighted="shero")
		#Agenda.objects.create(data="05/09/2017", hora_inicio="10:10:AM")

	def test_1(self):
		instance = Agenda.objects.values('data')[0]
		description = instance['description']
		self.assertEqual(description, '2018-05-19')

	def test_2(self):
		a = 1
		assert a == 2
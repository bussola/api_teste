from django.test import TestCase
from iclinicapp.models import Agenda
from django.contrib.auth.models import User
import datetime



class IclinicModelsTestCase(TestCase):
	def setUp(self):
		u = User(username="Jose")
		u.save()
		user = u
		Agenda.objects.create(data="2018-05-19", hora_inicio="10:10:AM", hora_final="10:10:AM", paciente="Jose", procedimento="Consulta", owner=user, highlighted="shero")

	def test_date(self):
		instance = Agenda.objects.values('data')[0]
		description = instance['data']
		self.assertEqual(description, datetime.date(2018, 5, 19))

	def test_2(self):
		a = 1
		assert a == 2
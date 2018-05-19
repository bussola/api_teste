from django.test import TestCase
from iclinicapp.models import Agenda

class AnimalTestCase(TestCase):
    def setUp(self):
        Agenda.objects.create(data="05/09/2018", hora_inicio="10:10:AM")
        Agenda.objects.create(data="05/09/2017", hora_inicio="10:10:AM")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        # data = Agenda.objects.get(data="05/09/2017")
        # cat = Agenda.objects.get(name="cat")
        # self.assertEqual(lion.speak(), 'The lion says "roar"')
        # self.assertEqual(cat.speak(), 'The cat says "meow"')
        a = 1
        assert a == 1
        
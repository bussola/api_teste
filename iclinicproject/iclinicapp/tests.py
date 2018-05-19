from django.test import TestCase
from iclinicapp.models import Agenda

import unittest

class TestBasic(unittest.TestCase):
    "Basic tests"
    def setUp(self):
        self.agenda = Agenda.objects.all()

    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_basic_2(self):
        a = 1
        assert a == 1
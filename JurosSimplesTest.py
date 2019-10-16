# coding=utf-8
# Desenvolvimento Romullo
# JurosSimplesTest.py

from unittest import TestCase
from JurosSimples import Juros

__author__ = 'Desenvolvimento Romullo'


class JurosSimplesTest(TestCase):
            # Define Métodos de Testes

            def testSimples(self):
                # Testa método
                calcJuros = Juros()
                calcJuros.capital = 16000
                calcJuros.taxa = 0.04
                calcJuros.n_periodos = 4
                self.assertEqual(2560, calcJuros.simples())





try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
from calculadora import soma, subtrai


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 10, 5),
            (100, 100, 200),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('2', 0)
    
    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(2, '0')

    def test_subtrai_10_e_5_deve_retornar_5(self):
        self.assertEqual(subtrai(10, 5), 5)

    def test_subtrai_menos_20_e_5_deve_retornar_menos_25(self):
        self.assertEqual(subtrai(-20, 5), -25)

    def teste_subtrai_varias_entradas(self):
        x_y_saidas = (
            (5, 4, 1),
            (10, 4, 6),
            (200, 100, 100),
            (-50, 4, -54),
            (100, 200, -100),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(subtrai(x, y), saida)

    def test_subtrai_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai('2', 0)
    
    def test_subtrai_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai(2, '0')

if __name__ == '__main__':
    unittest.main(verbosity=2)
  
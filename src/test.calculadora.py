import unittest
from calculadora import calcular


class TestCalcular(unittest.TestCase):

    def test_suma(self):
        valor_esperado = 3
        valor_actual = calcular(1, 2, '+')
        self.assertEqual(valor_esperado, valor_actual)

    def test_resta(self):
        valor_esperado = 2
        valor_actual = calcular(5, 3, '-')
        self.assertEqual(valor_esperado, valor_actual)

    def test_multiplicacion(self):
        valor_esperado = 12
        valor_actual = calcular(4, 3, '*')
        self.assertEqual(valor_esperado, valor_actual)

    def test_division(self):
        valor_esperado = 5.0
        valor_actual = calcular(10, 2, '/')
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_potencia(self):
        valor_esperado = 8
        valor_actual = calcular(2, 3, '^')
        self.assertEqual(valor_esperado, valor_actual)

    def test_modulo(self):
        valor_esperado = 1
        valor_actual = calcular(10, 3, '%')
        self.assertEqual(valor_esperado, valor_actual)

    def test_operacion_invalida(self):
        with self.assertRaises(ValueError):
            calcular(10, 5, 'x')

if __name__ == '__main__':
    unittest.main()
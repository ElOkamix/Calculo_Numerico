import unittest

from biseccion import metodo_biseccion
from newton_raphson import Newton_Raphson
from integ_num import suma_riemann

class TestMethods(unittest.TestCase):
     # Aquí escribes el código para probar la función biseccion
    def test_biseccion(self):
        root = metodo_biseccion(lambda x: x**2 - 4, 0, 3)
        self.assertAlmostEqual(root, 2)

    # Aquí escribes el código para probar la función newton_raphson
    def test_newton_raphson(self):
        root = Newton_Raphson(lambda x: x**2 - 4, 2)
        self.assertAlmostEqual(root, 2)

    # Aquí escribes el código para probar la función integracion_numerica
    def test_integracion_numerica(self):
        root = suma_riemann(lambda x: x**2 - 4, 2)
        self.assertAlmostEqual(root, 2)
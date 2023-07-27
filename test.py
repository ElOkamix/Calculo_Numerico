import unittest

#Importación de los métodos

from biseccion import biseccion
from newton_raphson import newton_raphson
from integ_num import suma_riemann
from integ_num import metodo_trapecio
from Ecuaciones_Dif import metodo_euler

#Clase con los testt

class TestMethods(unittest.TestCase):
     # Aquí el código para probar la función biseccion
    def test_biseccion(self):
        pass

    # Aquí el código para probar la función newton_raphson
    def test_newton_raphson(self):
        pass

    # Aquí el código para probar la función integracion_numerica
    def test_integracion_numerica(self):
        pass

    def test_integracion_numerica(self):
        pass

    #Aquí el código para probar la función Ecuaciones_Dif

    def test_ecuaciones_diferenciales(self):
        pass
        
        if __name__ == '__main__':
            unittest.main()
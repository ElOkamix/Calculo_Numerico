def suma_riemann(f, a, b, n):
    """
    Aproxima el valor de una integral definida utilizando el método de la suma de Riemann.
    
    Parámetros:
    f -- función a integrar
    a -- límite inferior de integración
    b -- límite superior de integración
    n -- número de subintervalos
    
    Retorna:
    acum -- aproximación numérica de la integral definida
    """
    
    h = (b-a)/n # Calcula el ancho de cada subintervalo
    acum = 0 # Inicializa el acumulador en cero
    
    for i in range(n):
        x = a + i*h # Calcula el punto x en el que se evaluará la función
        acum = acum + h * f(x) # Suma al acumulador el área del rectángulo
    
    return acum # Retorna la aproximación numérica de la integral definida

""" Acá el ejemplo de uso """

def f(x):
    return x ** 2

a = 0
b = 1
n = 100

resultado = suma_riemann(f, a, b, n)
print(resultado)
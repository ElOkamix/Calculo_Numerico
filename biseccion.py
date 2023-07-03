def metodo_biseccion(func, a, b, error=0.02, max_iterations=100):
    """
    Implementación del método de bisección para encontrar la raíz de una función.

    Args:
        func: Función objetivo para la cual se desea encontrar la raíz.
        a: Límite inferior del intervalo inicial.
        b: Límite superior del intervalo inicial.
        error: Error tolerado para el criterio de convergencia (por defecto, 0.02).
        max_iterations: Número máximo de iteraciones permitidas (por defecto, 100).

    Returns:
        La aproximación de la raíz de la función.
    """
    if func(a) * func(b) >= 0:
        raise ValueError("La función no cumple el criterio de cambio de signo en el intervalo dado.")
    
    for i in range(max_iterations):
        c = (a + b) / 2  # Punto medio del intervalo

        if abs(func(c)) < error or abs(b - a) < error:
            return c

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

    raise ValueError("El método no converge después de {} iteraciones.".format(max_iterations))

""" Acá el ejemplo de Uso """

def func(x):
    return x**2 - 4

# Especificación del intervalo inicial y los parámetros del método de bisección

a = 1
b = 3
error = 0.02
max_iterations = 10

# Llamada al método de bisección para encontrar la aproximación de la raíz

approx_root = metodo_biseccion(func, a, b, error, max_iterations)
print("Aproximación de la raíz: ", approx_root)

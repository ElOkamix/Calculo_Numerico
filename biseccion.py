def bisection_method(func, a, b, tolerance=1e-6, max_iterations=100):
    """
    Implementación del método de bisección para encontrar la raíz de una función.

    Args:
        func: Función objetivo para la cual se desea encontrar la raíz.
        a: Límite inferior del intervalo inicial.
        b: Límite superior del intervalo inicial.
        tolerance: Tolerancia para el criterio de convergencia (por defecto, 1e-6).
        max_iterations: Número máximo de iteraciones permitidas (por defecto, 100).

    Returns:
        La aproximación de la raíz de la función.
    """
    if func(a) * func(b) >= 0:
        raise ValueError("La función no cumple el criterio de cambio de signo en el intervalo dado.")

    for i in range(max_iterations):
        c = (a + b) / 2  # Punto medio del intervalo

        if abs(func(c)) < tolerance or abs(b - a) < tolerance:
            return c

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    raise ValueError("El método no converge después de {} iteraciones.".format(max_iterations))
def funcion(x):
    # Aquí define la función para la cual quieres encontrar las raíces
    return x**3 - 2*x**2 + 4*x - 8

def derivada(x):
    # Aquí define la derivada de la función
    return 3*x**2 - 4*x + 4

def newton_raphson(funcion, derivada, x_inicial, tolerancia=1e-6, max_iter=100):
    x_actual = x_inicial
    iteracion = 0

    while abs(funcion(x_actual)) > tolerancia and iteracion < max_iter:
        x_siguiente = x_actual - funcion(x_actual) / derivada(x_actual)
        x_actual = x_siguiente
        iteracion += 1

    return x_actual

# Ejemplo de uso:
punto_inicial = 1.5  # Puedes cambiar este valor como punto de partida
raiz_aproximada = newton_raphson(funcion, derivada, punto_inicial)

print("Raíz aproximada:", raiz_aproximada)
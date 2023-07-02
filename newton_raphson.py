from sympy import symbols, diff

def Newton_Raphson(f, x0, E, N):
    """
    Implementación del método de Newton-Raphson para encontrar la raíz de una función.

    Argumentos:
    f: Función para la cual se desea encontrar la raíz.
    x0: Valor inicial para comenzar la iteración.
    E: Tolerancia (error máximo aceptado).
    N: Número máximo de iteraciones.

    Retorna:
    x: Valor de la raíz encontrada.
    """
    
    x = x0
    for i in range(N):
        y = f(x)
        y_prime = diff(f, x)  # Calcula la derivada de f en x usando SymPy
        x_next = x - y / y_prime
        
        if abs(x_next - x) < E:
            return x_next
        
        x = x_next
    
    return x  # Retorna el valor de x después de N iteraciones si no se alcanza la tolerancia

# Ejemplo de uso
x = symbols('x')

def f(x):
    return x**2 - 4

x0 = 2  # Valor inicial
E = 0.02  # Tolerancia
N = 100  # Número máximo de iteraciones

raiz = Newton_Raphson(f, x0, E, N)
print("La raíz encontrada es:", raiz)
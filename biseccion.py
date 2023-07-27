import math

def biseccion(F, a, b, E, N):
    print("\nMetodo Biseccion\n")
    if F(a) * F(b) >= 0:
        print("El método de bisección no es aplicable en este intervalo.")
        return None
    
    # Inicializar variables
    n = 1
    error_relativo_aproximado = 100
    
    # Iteraciones del método de bisección
    while n <= N and error_relativo_aproximado > E:
        c = (a + b) / 2
        f_c = F(c)
        
        print(f"Iteración {n}:")
        print(f"a = {a}, b = {b}, c = {c}")
        print(f"F(c) = {f_c}")
        
        if F(a) * f_c < 0:
            b = c
        else:
            a = c
        
        if n > 1:
            error_relativo_aproximado = abs((c - c_anterior) / c)
        
        print(f"Error relativo aproximado: {error_relativo_aproximado}\n")
        
        c_anterior = c
        n += 1
    
    # Resultado final
    if n > N:
        print("El método de bisección no converge después de N iteraciones.")
    else:
        print(f"La aproximación de la raíz es {c} con un error relativo aproximado de {error_relativo_aproximado}")

# Ejemplo de uso
def F(x):
    return math.sin(x) - math.exp(-x)

a = 0
b = 1
E = 0.02
N = 100

biseccion(F, a, b, E, N)

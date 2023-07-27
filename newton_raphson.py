import sympy as sp

print("\nMetodo Newton Raphson\n")

def newton_raphson(F, x0, E, N):
    # Definir el símbolo x para la variable independiente
    x = sp.Symbol('x')
    
    # Convertir la expresión F en una expresión simbólica
    f = sp.sympify(F)
    
    # Calcular la derivada de la expresión F respecto a x
    f_prime = f.diff(x)
    
    # Convertir las expresiones simbólicas en funciones numéricas
    F = sp.lambdify(x, f)
    F_prime = sp.lambdify(x, f_prime)
    
    n = 1
    error_relativo = 100
    x_i = x0
    
    while n <= N and error_relativo > E:
        # Aplicar la fórmula de Newton-Raphson
        x_i_mas_1 = x_i - F(x_i) / F_prime(x_i)
        
        print(f"Iteración {n}:")
        print(f"x_{n} = {x_i}, x_{n+1} = {x_i_mas_1}")
        
        if n > 1:
            # Calcular el error relativo
            error_relativo = abs((x_i_mas_1 - x_i) / x_i_mas_1)
            
        print(f"Error relativo: {error_relativo}\n")
        
        x_i = x_i_mas_1
        n += 1
    
    if n > N:
        print("El método de Newton-Raphson no converge después de N iteraciones.")
    else:
        print(f"La aproximación de la raíz es {x_i_mas_1} con un error relativo de {error_relativo}")

# Ejemplo de uso
F = 'sin(x) - exp(-x)'
x0 = 1  # Valor inicial
E = 0.02  # Error relativo
N = 100  # Número máximo de iteraciones

newton_raphson(F, x0, E, N)
from scipy import integrate

def f(x):
    # Definir la función que quieres integrar
    return x**2

a = 0  # Límite inferior de integración
b = 1  # Límite superior de integración

# Realizar la integración numérica utilizando el método del trapecio
result = integrate.trapz(f, [a, b])

print("El resultado de la integración es:", result)
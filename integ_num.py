def suma_riemann(f, a, b, n):
    print('\nSuma de Riemann\n')
    h = (b-a)/n # Calculamos el ancho de cada subintervalo
    # Creamos una lista con los valores de x en cada subintervalo
    x = [a + i * h for i in range(n+1)]
    # Calculamos la suma de Riemann utilizando la lista de valores de x
    Acum = sum([h * f(xi) for xi in x])
    return Acum

def metodo_trapecio(f, a, b, n):
    print('\nMétodo del trapecio\n')
    h = (b-a)/n # Calculamos el ancho de cada subintervalo
    # Creamos una lista con los valores de x en cada subintervalo
    x = [a + i * h for i in range(n)]
    # Calculamos la suma utilizando el método del trapecio
    acum = sum([((f(xi) + f(xi+h)) * h)/2 for xi in x])
    return acum

print('\nIntegración numérica\n')
f = lambda x: (x+1)**0.5 # Definimos la función a integrar
X0 = -1 # Límite inferior de integración
Xn= 1 # Límite superior de integración
n= 5 # Número de subintervalos
resultado = suma_riemann(f, X0, Xn, n) # Calculamos la suma de Riemann
print('El resultado es:', resultado)
resultado = metodo_trapecio(f, X0, Xn, n) # Calculamos la suma utilizando el método del trapecio
print('El resultado es:', resultado)

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

def trapecio(f, a, b, n):
    """
    Aproxima el valor de una integral definida utilizando el método del trapecio.
    
    Parámetros:
    f -- función a integrar
    a -- límite inferior de integración
    b -- límite superior de integración
    n -- número de subintervalos
    
    Retorna:
    aprox -- aproximación numérica de la integral definida
    """
    
    h = (b-a)/n # Calcula el ancho de cada subintervalo
    aprox = 0.5 * (f(a) + f(b)) # Inicializa el acumulador con los valores de los extremos
    
    for i in range(1, n):
        x = a + i*h # Calcula el punto x en el que se evaluará la función
        aprox += f(x) # Suma al acumulador el valor de la función en x
    
    aprox *= h # Multiplica el acumulador por el ancho de los subintervalos
    
    return aprox # Retorna la aproximación numérica de la integral definida


""" Acá el ejemplo de uso de suma_riemann """

def f(x):
    return x ** 2

a = 1  # Límite inferior del intervalo de integración
b = 3  # Límite superior del intervalo de integración
n = 100  # Número de subdivisiones del intervalo

resultado = suma_riemann(f, a, b, n)
print(resultado)

""" Acá el ejemplo de uso de trapecio """

# Define la función a integrar
def f(x):
    return x**2

# Establece los límites de integración y el número de subintervalos
a = 0
b = 1
n = 10

# Calcula la aproximación numérica de la integral definida
aprox = trapecio(f, a, b, n)

# Imprime el resultado
print("La aproximación numérica de la integral definida es:", aprox)


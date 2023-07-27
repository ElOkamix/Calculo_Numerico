def metodo_euler(derivada_y, y_inicial, h, n):
    print("\nMétodo Euler\n")
    # Inicializar listas para almacenar los valores de la tabla
    valores_i = []
    valores_t = []
    valores_y = []

    # Añadir los valores iniciales a las listas
    valores_i.append(0)
    valores_t.append(1)
    valores_y.append(y_inicial)

    # Iterar usando el método de Euler
    for i in range(1, n + 1):
        t_i = valores_t[i - 1] + h
        y_i = valores_y[i - 1] + h * derivada_y(valores_t[i - 1], valores_y[i - 1])

        # Agregar los valores calculados a las listas
        valores_i.append(i)
        valores_t.append(t_i)
        valores_y.append(y_i)

    # Imprimir la tabla
    print("i   |   ti   |   yi   |   yi+1")
    print("-----------------------------")
    for i, t_i, y_i, y_siguiente in zip(valores_i, valores_t, valores_y, valores_y[1:]):
        print(f"{i}   |  {t_i:.2f}  |  {y_i:.6f}  |  {y_siguiente:.6f}")

# Función y'(t) = t/y
def derivada_y(t, y):
    return t / y

# Condiciones iniciales
y_inicial = 2
h = 0.2
n = 6  # Cambiado a 6 para una iteración adicional

# Calcular y mostrar la solución usando el método de Euler
metodo_euler(derivada_y, y_inicial, h, n)

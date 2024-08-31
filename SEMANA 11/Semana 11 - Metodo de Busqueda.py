# Definir la matriz bidimensional (3x3)
matriz = [
    [4, 7, 1],
    [9, 3, 8],
    [6, 5, 2]
]

def buscar_valor(matriz, valor_a_buscar):
    # Recorrer filas y columnas de la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_a_buscar:
                # Si se encuentra el valor, mostrar su posición
                return f"Valor {valor_a_buscar} encontrado en la posición ({i}, {j})"
    # Si el valor no se encuentra en la matriz
    return f"Valor {valor_a_buscar} no encontrado en la matriz."

# Definir el valor a buscar
valor_a_buscar = 5

# Llamar a la función y mostrar el resultado
resultado = buscar_valor(matriz, valor_a_buscar)
print(resultado)

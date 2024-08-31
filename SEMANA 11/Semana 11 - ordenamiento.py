# Definir la matriz bidimensional (3x3)
matriz = [
    [9, 3, 5],
    [6, 8, 2],
    [7, 4, 1]
]

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

def ordenar_fila(matriz, fila_index):
    # Mostrar la matriz original
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    # Ordenar la fila específica usando Bubble Sort
    bubble_sort(matriz[fila_index])

    # Mostrar la matriz con la fila ordenada
    print("\nMatriz con la fila", fila_index, "ordenada:")
    for fila in matriz:
        print(fila)

# Definir el índice de la fila a ordenar (por ejemplo, la fila 1)
fila_index = 1

# Llamar a la función para ordenar la fila específica
ordenar_fila(matriz, fila_index)

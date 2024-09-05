import random

# Definir los datos: ciudades, días de la semana, semanas
ciudades = ["Guayaquil", "Ambato", "Napo"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Por ejemplo, cuatro semanas de datos

# Crear una matriz 3D (ciudades x semanas x días de la semana) con datos de temperatura aleatorios
temperaturas = [[[random.uniform(10.0, 30.0) for _ in range(len(dias_semana))] for _ in range(semanas)] for _ in ciudades]

# Mostrar las temperaturas diarias y calcular el promedio por semana
for i, ciudad in enumerate(ciudades):
    print(f"\nTemperaturas para {ciudad}:")
    for semana in range(semanas):
        print(f"\n  Semana {semana + 1}:")
        suma_semana = 0
        for dia in range(len(dias_semana)):
            temp_dia = temperaturas[i][semana][dia]
            print(f"    {dias_semana[dia]}: {temp_dia:.2f}°C")
            suma_semana += temp_dia
        promedio_semana = suma_semana / len(dias_semana)
        print(f"  Promedio de la semana {semana + 1}: {promedio_semana:.2f}°C")

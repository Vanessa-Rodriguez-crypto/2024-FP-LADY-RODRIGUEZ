import random


# Función para calcular el promedio de temperatura de una ciudad
def calcular_promedio_temperaturas(temperaturas, ciudades, dias_semana, semanas):

    """La función muestra las temperaturas diarias para cada ciudad y semana,
    y luego calcula y devuelve el promedio de temperatura de cada ciudad durante todas las semanas.
    """

    promedios_ciudades = []  # Lista para almacenar el promedio de cada ciudad

    # Iterar sobre cada ciudad
    for i, ciudad in enumerate(ciudades):
        print(f"\nTemperaturas para {ciudad}:")
        suma_total_ciudad = 0  # Acumulador para la suma de todas las temperaturas de la ciudad

        # Iterar sobre las semanas
        for semana in range(semanas):
            print(f"\n  Semana {semana + 1}:")
            suma_semana = 0  # Acumulador para la suma de las temperaturas de la semana

            # Iterar sobre los días de la semana
            for dia in range(len(dias_semana)):
                temp_dia = temperaturas[i][semana][dia]
                print(f"    {dias_semana[dia]}: {temp_dia:.2f}°C")
                suma_semana += temp_dia  # Sumar la temperatura del día a la suma de la semana

            promedio_semana = suma_semana / len(dias_semana)  # Promedio de la semana
            print(f"  Promedio de la semana {semana + 1}: {promedio_semana:.2f}°C")

            # Sumar la temperatura promedio semanal a la suma total de la ciudad
            suma_total_ciudad += suma_semana

        # Calcular el promedio general de la ciudad durante todas las semanas
        promedio_ciudad = suma_total_ciudad / (semanas * len(dias_semana))
        promedios_ciudades.append(promedio_ciudad)  # Almacenar el promedio de la ciudad
        print(f"\nPromedio general de {ciudad}: {promedio_ciudad:.2f}°C\n")

    return promedios_ciudades


# Definir los datos: ciudades, días de la semana, semanas
ciudades = ["Guayaquil", "Ambato", "Napo"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Por ejemplo, cuatro semanas de datos

# Crear una matriz 3D (ciudades x semanas x días de la semana) con datos de temperatura aleatorios
temperaturas = [[[random.uniform(10.0, 30.0) for _ in range(len(dias_semana))] for _ in range(semanas)] for _ in
                ciudades]

# Llamar a la función para calcular y mostrar los promedios
promedios = calcular_promedio_temperaturas(temperaturas, ciudades, dias_semana, semanas)

# Mostrar el promedio de cada ciudad
for ciudad, promedio in zip(ciudades, promedios):
    print(f"El promedio de temperatura en {ciudad} durante el período es: {promedio:.2f}°C")

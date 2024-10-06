# Escritura en un archivo de texto
# Creamos un archivo llamado my_notes.txt
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales
    file.write("Nota 1: Aprender a programar en Python.\n")
    file.write("Nota 2: Practicar más ejercicios de archivos.\n")
    file.write("Nota 3: Revisar temas avanzados de Python.\n")

# Lectura de un archivo de texto
# Abrimos el archivo my_notes.txt para leerlo
with open('my_notes.txt', 'r') as file:
    # Leemos línea por línea usando un bucle
    for line in file:
        # Mostramos cada línea en la consola
        print(line.strip())  # .strip() elimina saltos de línea extra al mostrar

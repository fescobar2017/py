import csv

# Datos a guardar en el archivo CSV
datos_matriz = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Luis', 30, 'Santiago'],
    ['Ana', 25, 'Valparaíso'],
    ['Carlos', 40, 'Concepción']
]

# Escritura del archivo CSV con codificación
with open('datos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(datos_matriz)

# Lectura del archivo CSV
with open('datos.csv', 'r') as file:
    reader = csv.reader(file)
    for fila in reader:
        print(fila)


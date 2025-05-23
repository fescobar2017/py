import csv

datos_matriz = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Luis', 30, 'Santiago'],
    ['Ana', 25, 'Valparaíso'],
    ['Carlos', 40, 'Concepción']
]

with open('datos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(datos_matriz)

with open('datos.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for fila in reader:
        print(fila)

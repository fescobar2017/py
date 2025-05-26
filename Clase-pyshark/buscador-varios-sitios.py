import pyshark
import csv
from collections import Counter

INTERFAZ = 'any'
capture = pyshark.LiveCapture(interface=INTERFAZ, display_filter='dns')

resultados_dns = []
cantidad = 0
print("🔍 Escuchando tráfico DNS...\n")

for packet in capture:
    try:
        if hasattr(packet, 'dns') and hasattr(packet.dns, 'qry_name'):
            query_name = packet.dns.qry_name.lower()
            print(f"Consulta DNS detectada: {query_name}")
            resultados_dns.append(query_name)
            cantidad += 1
        if cantidad == 100:
            break
    except AttributeError:
        pass

# Contar y obtener top 5 con Counter
frecuencias = Counter(resultados_dns)
top5 = frecuencias.most_common(5)

# Guardar en CSV
with open('resultados_dns.csv', mode='w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(['Dominio', 'Repeticiones'])
    escritor.writerows(top5)

# Mostrar el contenido del CSV
print('''\nContenido del archivo resultados_dns.csv:\nAbriendo file....\n''')
with open('resultados_dns.csv', mode='r') as archivo_csv:
    for linea in archivo_csv:
        print(linea)

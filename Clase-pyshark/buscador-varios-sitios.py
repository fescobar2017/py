import pyshark
import csv
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
            cantidad = cantidad + 1
        if cantidad == 1000:
            break
    except AttributeError:
        pass

# Paso 1: Contar repeticiones
frecuencias = {}

for dominio in resultados_dns:
    if dominio in frecuencias:
        frecuencias[dominio] += 1
    else:
        frecuencias[dominio] = 1

# Paso 2: Encontrar el top 5 manualmente
top5 = []

for _ in range(5):
    max_dominio = None
    max_veces = -1
    for dominio, veces in frecuencias.items():
        if veces > max_veces and dominio not in [d for d, _ in top5]:
            max_dominio = dominio
            max_veces = veces
    if max_dominio:
        top5.append((max_dominio, max_veces))

with open('resultados_dns.csv', mode='w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv, delimiter=',')
    escritor.writerow(['Consultas DNS'])      
    escritor.writerow(top5)          


print(''' Contenido del archivo        
         Resultados_dns.csv:
         Abriendo file ....
          ''')

with open('resultados_dns.csv', mode='r') as archivo_csv:
    for linea in archivo_csv:
        print(linea.strip())
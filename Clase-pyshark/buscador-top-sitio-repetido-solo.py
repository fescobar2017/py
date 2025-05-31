#busca sitios repetidos
import pyshark
import csv
from collections import Counter
INTERFAZ = 'any'
capture = pyshark.LiveCapture(interface=INTERFAZ,display_filter='dns')
cantidad = 0
resultados_dns = []
print (" Escuchando peticiones DNS ")
for packet in capture:
    try:
        if hasattr(packet,'dns') and hasattr(packet.dns,'qry_name'):
            query_name = packet.dns.qry_name.lower()
            print(f"Consulta dns detectada a {query_name}")
            resultados_dns.append(query_name)
            cantidad += 1
        if cantidad == 40:
            break
    except AttributeError:
        pass
frecuencia = Counter(resultados_dns)
top_5 = frecuencia.most_common(5)
with open ('resultados_dns.csv',mode='w',newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerows(top_5)

print("5 top Sites \n")
num = 1
with open('resultados_dns.csv',mode='r') as archivo_csv:
    for linea in archivo_csv:
        print(f"TOP-{num}) {linea}")
        num += 1
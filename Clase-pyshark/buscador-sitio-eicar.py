import pyshark
import csv
INTERFAZ = 'any'

capture = pyshark.LiveCapture(interface=INTERFAZ, display_filter='dns')

resultados_dns = []

print("Escuchando tráfico DNS...\n")


for packet in capture:
    try:
        if hasattr(packet, 'dns') and hasattr(packet.dns, 'qry_name'):
            query_name = packet.dns.qry_name.lower()
            print(f"Consulta DNS detectada: {query_name}")
            resultados_dns.append(query_name)
            
            
            if 'eicar' in query_name:
                print(" Tráfico hacia eicar detectado. Finalizando captura.")
                break
    except AttributeError:
        pass


with open('resultados_dns.csv', mode='w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv, delimiter=',')
    escritor.writerow(['Consultas DNS'])      
    escritor.writerow(resultados_dns)          


print(''' Contenido del archivo 
         
         Resultados_dns.csv:
         Abriendo file ....
         ....
          
      ''')

with open('resultados_dns.csv', mode='r') as archivo_csv:
    for linea in archivo_csv:
        print(linea.strip())


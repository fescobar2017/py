# Cargar captura y filtrar por TCP o UDP hacia esas IPs, tambien las Flags, datos deben ser guardado en un csv, mostrar IP de origen y destino tambien
#    "69.163.33.82",
#    "87.106.139.101",
#    "mixunderax.com",
#    "alforcargo.com",
#    "181.113.229.139",
#    "159.65.241.220"
#  ALUMNO FRANCISCO ESCOBAR ROA
import csv
import pyshark

capture = pyshark.FileCapture('/home/francisco/Escritorio/Python/Clase-pyshark/pesadilla.pcapng',display_filter='tcp or udp')

listaip = ['69.163.33.82', '87.106.139.101', '181.113.229.139', '159.65.241.220']
listadns = ['mixunderax.com', 'alforcargo.com']
trafico = []

for packet in capture:
    try:
        iporigen = packet.ip.src
        ipdestino = packet.ip.dst
        protocolo = packet.transport_layer
        flags = packet.tcp.flags if protocolo == 'TCP' and hasattr(packet.tcp, 'flags') else 'N/A'

        # Verificación por IP
        if iporigen in listaip or ipdestino in listaip:
            print(f"[IP] {iporigen} -> {ipdestino} | Protocolo: {protocolo} | Flags: {flags}")
            trafico.append([iporigen, ipdestino, protocolo, flags])

        # Verificación por dominio
        if 'dns' in packet and hasattr(packet.dns, 'qry_name'):
            sitio = packet.dns.qry_name.lower()
            if any(dominio in sitio for dominio in listadns):
                print(f"[DNS] {iporigen} -> {sitio}")
                trafico.append([iporigen, sitio, 'DNS', 'N/A'])

    except AttributeError:
        continue

# Guardar CSV
with open('resultados.csv', mode='w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(['IP Origen', 'IP Destino/Dominio', 'Protocolo', 'Flags'])
    escritor.writerows(trafico)

print(" Tráfico guardado en resultados.csv")


import csv
import pyshark


def funcion1():
    capture = pyshark.FileCapture('/home/francisco/Escritorio/Python/Clase-pyshark/pesadilla.pcapng',display_filter='dns.qry.name or tcp.flags == 0x11')
    resultados = []
    for packet in capture:
        if hasattr(packet,'ip'):
            ip_origen = packet.ip.src
            ip_destino = packet.ip.dst
            
          # Si es paquete DNS
        if 'dns' in packet and hasattr(packet.dns, 'qry_name'):  
            if 'dns' in packet and hasattr(packet.dns, 'qry_name'):
                dominio = packet.dns.qry_name.lower()
                print(f"[DNS] {ip_origen} → {dominio}")
                resultados.append([ip_origen, dominio, 'TIPO DNS'])

        # Si es paquete TCP con flags FIN y ACK
        if hasattr(packet, 'tcp') and hasattr(packet.tcp, 'flags'):
            if packet.tcp.flags == '0x0011':
                print(f"[FIN-ACK] {ip_origen} → {ip_destino} | Flags: {packet.tcp.flags}")
                resultados.append([ip_origen, ip_destino, 'TIPO FIN-ACK']) 
    
    print(f"Total de resultados: {len(resultados)}")
    with open('opcion1.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['IP Origen', 'IP Destino/Dominio', 'Tipo'])
        writer.writerows(resultados)
    print(" DATOS GUARDADOS EN opcion1.csv")
    print('='*30)
    capture.close()

def funcion2():
    listaip = ['69.163.33.82', '87.106.139.101', '181.113.229.139', '159.65.241.220']
    listadns = ['mixunderax.com', 'alforcargo.com']
    capture = pyshark.FileCapture('/home/francisco/Escritorio/Python/Clase-pyshark/pesadilla.pcapng',display_filter='dns or tcp.flags or udp') 
    trafico = []

    for packet in capture:
        if hasattr(packet, 'ip') and hasattr(packet, 'transport_layer'):
            iporigen = packet.ip.src
            ipdestino = packet.ip.dst
            protocolo = packet.transport_layer
            flags = packet.tcp.flags if protocolo == 'TCP' and hasattr(packet.tcp, 'flags') else 'N/A'
            if protocolo == 'UDP' and ipdestino in listaip:
                print(f"IP-UDP {iporigen} -> {ipdestino}")
                trafico.append([iporigen, ipdestino,"UDP"])
        # Verificación por IP
            if ipdestino in listaip:
                print(f"[IP] {iporigen} -> {ipdestino} | Flags: {flags}")
                trafico.append([iporigen, ipdestino, protocolo, flags])

        # Verificación por dominio
            if 'dns' in packet and hasattr(packet.dns, 'qry_name'):
                sitio = packet.dns.qry_name.lower()
                if any(dominio in sitio for dominio in listadns):
                    print(f"[DNS] {iporigen} -> {sitio}")
                    trafico.append([iporigen, sitio, 'DNS'])



# Guardar CSV
    with open('opcion2.csv', mode='w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(['IP Origen', 'IP Destino/Dominio', 'Protocolo', 'Flags'])
        escritor.writerows(trafico)

    print(" DATOS GUARDADOS EN opcion2.csv")
    print('='*30)
    capture.close()       

def funcion3():
    listaip = ['69.163.33.82', '87.106.139.101', '181.113.229.139', '159.65.241.220']
    listadns = ['mixunderax.com', 'alforcargo.com']
    capture = pyshark.FileCapture('/home/francisco/Escritorio/Python/Clase-pyshark/pesadilla.pcapng',display_filter='dns or tcp.flags or udp') 
    trafico = []

    for packet in capture:
        if hasattr(packet, 'ip') and hasattr(packet, 'transport_layer'):
            iporigen = packet.ip.src
            ipdestino = packet.ip.dst
            protocolo = packet.transport_layer
            flags = packet.tcp.flags if protocolo == 'TCP' and hasattr(packet.tcp, 'flags') else 'N/A'
            if protocolo == 'UDP' and ipdestino in listaip:
                print(f"IP-UDP {iporigen} -> {ipdestino}")
                trafico.append([iporigen, ipdestino,"UDP"])
        # Verificación por IP
            if ipdestino in listaip:
                print(f"[IP] {iporigen} -> {ipdestino} | Flags: {flags}")
                trafico.append([iporigen, ipdestino, protocolo, flags])

        # Verificación por dominio
            if 'dns' in packet and hasattr(packet.dns, 'qry_name'):
                sitio = packet.dns.qry_name.lower()
                if any(dominio in sitio for dominio in listadns):
                    print(f"[DNS] {iporigen} -> {sitio}")
                    trafico.append([iporigen, sitio, 'DNS'])


def funcion4():
    capture = pyshark.FileCapture('/home/francisco/Escritorio/Python/Clase-pyshark/pesadilla.pcapng',display_filter='udp and not dns')
    trafico = []
    for packet in capture:
        if hasattr(packet, 'ip') and hasattr(packet, 'transport_layer'):
            iporigen = packet.ip.src
            ipdestino = packet.ip.dst
            protocolo = packet.transport_layer
            if protocolo == 'UDP':
                print(f"IP-UDP {iporigen} -> {ipdestino}")
                trafico.append([iporigen, ipdestino,"UDP"])

    with open('opcion4.csv', mode='w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(['IP Origen', 'IP Destino/Dominio', 'Protocolo'])
        escritor.writerows(trafico)

while True:
    print(" MENU ")
    print("======")
    print("(1) Capturar tráfico DNS y TCP FIN-ACK, guardar en CSV")
    print("(2) Cargar captura y filtrar por TCP o UDP hacia IPs sospechosas, guardar con Flags en CSV")
    print("(3) Cargar captura y filtrar por TCP o UDP hacia IPs sospechosas (solo mostrar)")
    print("(4) Capturar paquetes UDP (que no sean DNS), guardar en CSV")
    print("(0) Salir")

    try:
        opcion = int(input("Elija su opción: "))

        if opcion == 0:
            print("Saliendo del programa...")
            break
        elif opcion == 1:
            print("Ejecutando opción 1...")
            funcion1()
            
          
        elif opcion == 2:
            print("Ejecutando opción 2...")
            funcion2()
          
        elif opcion == 3:
            print("Ejecutando opción 3...")
         
            funcion3()

        elif opcion == 4:
            print("Ejecutando opción 4...")
           
            funcion4()
        else:
            print("Opción inválida. Elija entre 0 y 4.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")







        




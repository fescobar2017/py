import pyshark
import csv

def funcion1():
    print("Entrando en Opcion1")
    capture = pyshark.FileCapture('pesadilla.pcapng',display_filter='tcp.flags == 0x11 or dns')
    trafico1 =[]    
    for packet in capture:
        try:
            iporigen = packet.ip.src
            ipdestino = packet.ip.dst
            if hasattr(packet, 'dns') and hasattr(packet.dns, 'qry_name'):
                dns = packet.dns.qry_name
                print(f"[DNS] Trafico detectado DNS {dns}")
                trafico1.append([iporigen,ipdestino,dns])
            
            if hasattr(packet, 'tcp') and hasattr(packet.tcp, 'flags'):
                bandera = packet.tcp.flags
                print(f"[FIN-ACK] Detectado {iporigen} -> {ipdestino} | FLAGS {bandera}")
                trafico1.append([iporigen,ipdestino,bandera])
            
        except AttributeError:
                    pass
    with open ('funcion1.csv',mode='w',newline=(''))as archivo:
        escritor =csv.writer(archivo)
        escritor.writerow(['IP-ORIGEN','IP-DESTINO','DNS/FLAGS'])
        escritor.writerows(trafico1)
        print("TRAFICO GUARDADO EN funcion1.csv")
                       
    capture.close()
def funcion2():
    print("Entrando en Opcion2")
    listaip = ['69.163.33.82', '87.106.139.101', '181.113.229.139', '159.65.241.220']
    listadns = ['mixunderax.com', 'alforcargo.com']
    capture = pyshark.FileCapture('pesadilla.pcapng',display_filter='dns or ip.dst==69.163.33.82 or ip.dst==87.106.139.101 or ip.dst==181.113.229.139 or ip.dst==159.65.241.220')
    trafico2 =[]
    for packet in capture:
        try:
            if hasattr(packet, 'ip') and hasattr(packet.ip, 'dst'):
                iporigen = packet.ip.src
                ipdestino = packet.ip.dst
            if ipdestino in listaip:
                 print(f" Trafico detectado hacia {ipdestino}")
                 if hasattr(packet,'tcp') and hasattr(packet.tcp,'flags'):
                    bandera = packet.tcp.flags
                    trafico2.append([iporigen,ipdestino,bandera])
            if hasattr(packet,'dns') and hasattr(packet.dns,'qry_name'):
                 dns = packet.dns.qry_name
                 if dns in listadns:
                    print(f" Traficio detectado {dns}")
                    trafico2.append([iporigen,ipdestino,dns])
        except AttributeError:
             pass
        
    with open ('funcion2.csv',mode='w',newline=(''))as archivo:
        escritor =csv.writer(archivo)
        escritor.writerow(['IP-ORIGEN','IP-DESTINO','DNS/FLAGS'])
        escritor.writerows(trafico2)
        print("TRAFICO GUARDADO EN funcion2.csv")
    capture.close()                                           
def funcion3():
    print("Entrando en Opcion3")
    listaip = ['69.163.33.82', '87.106.139.101', '181.113.229.139', '159.65.241.220']
    listadns = ['mixunderax.com', 'alforcargo.com']
    capture = pyshark.FileCapture('pesadilla.pcapng',display_filter='dns or ip.dst==69.163.33.82 or ip.dst==87.106.139.101 or ip.dst==181.113.229.139 or ip.dst==159.65.241.220')
    
    for packet in capture:
        try:
            if hasattr(packet, 'ip') and hasattr(packet.ip, 'dst'):
                ipdestino = packet.ip.dst
                if ipdestino in listaip:
                    if hasattr(packet,'ip') and hasattr(packet.ip,'dst'):
                        print(f" Trafico detectado hacia {ipdestino}")                   
            if hasattr(packet,'dns') and hasattr(packet.dns,'qry_name'):
                 dns = packet.dns.qry_name
                 if dns in listadns:
                    print(f" Traficio detectado {dns}")
        except AttributeError:            
            pass
    capture.close()    
def funcion4():
    print("Entrando en Opcion4")
    trafico4 =[]
    capture = pyshark.FileCapture('pesadilla.pcapng',display_filter='udp and not dns')
    for packet in capture:
        try:
            if hasattr(packet,'udp'):
                iporigen = packet.ip.src
                ipdestino = packet.ip.dst
                print(f"Trafico UDP Detectado {iporigen} -> {ipdestino}")
                trafico4.append([iporigen,ipdestino,"UDP"])
        except AttributeError:
            pass
    with open ('funcion4.csv',mode='w',newline=(''))as archivo:
        escritor =csv.writer(archivo)
        escritor.writerow(['IP-ORIGEN','IP-DESTINO'])
        escritor.writerows(trafico4)
        print("TRAFICO GUARDADO EN funcion4.csv")            

    capture.close()
while True:
    print(" MENU ")
    print("======")
    print("(1) Capturar tráfico DNS y TCP FIN-ACK, guardar en CSV")
    print("(2) Cargar captura y filtrar por TCP o UDP hacia IPs sospechosas, guardar con Flags en CSV")
    print("(3) Cargar captura y filtrar por TCP o UDP hacia IPs sospechosas (solo mostrar)")
    print("(4) Capturar paquetes UDP (que no sean DNS), guardar en CSV")
    print("(0) Salir")

    opcion = int(input(" Favor ingre su opcion = "))
    
    if opcion == 0 : break
    if opcion == 1 : funcion1()
    if opcion == 2 : funcion2()
    if opcion == 3 : funcion3()
    if opcion == 4 : funcion4() 
    

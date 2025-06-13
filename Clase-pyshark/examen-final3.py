import pyshark
import csv


def funcion1():
    print("Entrando a Opcion 1")
    trafico1 = []
    capture = pyshark.FileCapture('pesadilla.pcapng',display_filter='dns or tcp.flags==0x11')
    
    for pkt in capture:
        try:
            iporigen = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None
            ipdestino = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst') else None
                             
            if hasattr(pkt,'dns') and hasattr(pkt.dns,'qry_name'):
                dominio = pkt.dns.qry_name
                print(f"[DNS] {iporigen} hacia {dominio} detectado")
                trafico1.append([iporigen,ipdestino,dominio])
            if hasattr(pkt,'tcp') and hasattr(pkt.tcp,'flags'):
                bandera = pkt.tcp.flags
                print(f"[FIN-ACK] {iporigen} |{ipdestino} | {bandera}")
                trafico1.append([iporigen,ipdestino,bandera])    
        except AttributeError as  error :
            print(f"[Error de Atributo] {error} en paquete {pkt.number}")
            pass
    with open('funcion1.csv',mode ='w',newline=('')) as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["IPORIGEN","IPDESTINO","DNS/FLAGS"])
        escritor.writerows(trafico1)
        print("TRAFICO GUARDASO EN funcion1.csv")

def funcion2():
    print("Entrando a Opcion 2")
    listaip = ['69.163.33.82', '87.106.139.101', '181.113.229.139', '159.65.241.220']
    listadns = ['mixunderax.com', 'alforcargo.com']
    trafico2 =[]
    capture = pyshark.FileCapture('pesadilla.pcapng',display_filter='dns or ip.dst==69.163.33.82 or ip.dst==87.106.139.101 or ip.dst==181.113.229.139 or ip.dst==159.65.241.220')

    for pkt in capture:

        try:
            
            iporigen = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None 
            ipdestino = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst') else None
            bandera = pkt.tcp.flags if hasattr(pkt,'tcp') and hasattr(pkt.tcp,'flags') else None
                
            if ipdestino in listaip:
                print(f"[IP-Malisiocsa] {iporigen} -> {ipdestino} | {bandera}")
                trafico2.append([iporigen,ipdestino,bandera,'IP MALISIOSA'])

            
            dominio = pkt.dns.qry_name if hasattr(pkt,'dns') and hasattr(pkt.dns,'qry_name') else None
                
                
            if dominio in listadns:
                    print(f"[DNS-Malisioso] {iporigen} -> {dominio}")
                    trafico2.append([iporigen,dominio,"DNS MALISIOSO"])
                

        except AttributeError as  error :
            print(f"[Error de Atributo] {error} en paquete {pkt.number}")
            pass
    with open('funcion2.csv',mode ='w',newline=('')) as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["IPORIGEN","IPDESTINO","DNS/FLAGS"])
        escritor.writerows(trafico2)
        print("🤖 TRAFICO GUARDASO EN funcion2.csv")    
            
def funcion3():
    print("Entrando a Opcion 3")
    listaip = ['69.163.33.82', '87.106.139.101', '181.113.229.139', '159.65.241.220','64.233.186.94']
    listadns = ['mixunderax.com', 'alforcargo.com']
    trafico3 =[]
    capture = pyshark.FileCapture('pesadilla.pcapng',display_filter='dns or ip.dst==69.163.33.82 or ip.dst==87.106.139.101 or ip.dst==181.113.229.139 or ip.dst==159.65.241.220')
    
    for pkt in capture:
        try:
            iporigen = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None             
            ipdestino = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst') else None
                
            if hasattr(pkt,'tcp') and hasattr(pkt.tcp,'flags'):
                bandera = pkt.tcp.flags
                if ipdestino in listaip:
                    print(f"{chr(0x1F928)}[TCP-IP-Malisiosa  ] {iporigen} hacia {ipdestino} | {bandera}")
                    print('-'*65)
                    trafico3.append([iporigen,ipdestino,bandera,'IP MALISIOSA'])

            if hasattr(pkt, 'udp') and ipdestino in listaip:
                print(f"{chr(0x1F928)}[UDP-IP-Malisiosa] {iporigen} -> {ipdestino}")
                print('-'*65)
                trafico3.append([iporigen,ipdestino,"UDP",'IP MALISIOSA'])


            dominio = pkt.dns.qry_name if hasattr(pkt,'dns') and hasattr(pkt.dns,'qry_name') else None
              
                
            if dominio in listadns:
                print(f"{chr(0x1F928)}[DNS-Malisioso     ] {iporigen} hacia {dominio}")
                print('-'*65)
                trafico3.append([iporigen,dominio,"DNS MALISIOSO"])
                

        except AttributeError as  error :
            print(f"[Error de Atributo] {error} en paquete {pkt.number}")
            pass

def funcion4():
    print("Entrando a Opcion 4")
    trafico4 =[]
    capture = pyshark.FileCapture('pesadilla.pcapng',display_filter='udp and not dns')

    for pkt in capture:
        try:
            iporigen = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None
            ipdestino = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst')else None
                

            if hasattr(pkt,'udp'):
                print(f"[UDP] {iporigen} -> {ipdestino}")
                trafico4.append(["UPD",iporigen,ipdestino])
               

        except AttributeError as  error :
            print(f"[Error de Atributo] {error} en paquete {pkt.number}")
            pass
    with open('funcion4.csv',mode ='w',newline=('')) as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["IPORIGEN","IPDESTINO"])
        escritor.writerows(trafico4)
        print("💬 TRAFICO GUARDADO EN funcion4.csv")         

while True:

    print("Menu")
    print("====")
    print("(1) Capturar tráfico DNS y TCP FIN-ACK, guardar en CSV")
    print("(2) Cargar captura y filtrar por TCP o UDP hacia IPs sospechosas, guardar con Flags en CSV")
    print("(3) Cargar captura y filtrar por TCP o UDP hacia IPs sospechosas (solo mostrar)")
    print("(4) Capturar paquetes UDP (que no sean DNS), guardar en CSV")
    print("(0) Salir")

    opcion =int(input("Ingrese su opcion = "))
    
    if opcion == 1 : funcion1()
    if opcion == 2 : funcion2()
    if opcion == 3 : funcion3()
    if opcion == 4 : funcion4()
    if opcion == 0 : break
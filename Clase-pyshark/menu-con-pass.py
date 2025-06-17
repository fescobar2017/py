import pyshark
import random
import csv

usersesion = "a"
passsesion = "b"

def funcion1():
    trafico1 =[]
    print("Entrando a funcion 1")
    print(" Busca los dns visitados en 100 Paquetes ")
    capture = pyshark.LiveCapture('any',display_filter='dns')
    for pkt in capture.sniff_continuously(packet_count=100):
         try:
              iporigen = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None
              ipdestino = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst') else None
              srcport = pkt.udp.srcport if hasattr(pkt,'udp') and hasattr(pkt.udp,'srcport') else None
              dstport = pkt.udp.dstport if hasattr(pkt,'udp') and hasattr(pkt.udp,'dstport') else None
                
              if hasattr(pkt,'dns') and hasattr(pkt.dns,'qry_name'):
                   dns = pkt.dns.qry_name
                   print (f"[DNS] {iporigen}:{srcport} -> {ipdestino}:{dstport} | {dns}")
                   trafico1.append([iporigen,srcport,ipdestino,dstport,dns])
         except AttributeError as error:
              print(f"[ERROR] {error}")
    with open('funcion1.csv',mode ='w',newline = '') as archivo_cvs:
         escritor = csv.writer(archivo_cvs)               
         escritor.writerows(trafico1)
         print(f"Trafico guardado en funcion1.csv")

def funcion2():
    print("Entrando a funcion 2")
    print("Detecta PING en 100 Paquetes")
    trafico2 = []
    capture = pyshark.LiveCapture('any',display_filter='icmp')
    for pkt in capture.sniff_continuously(packet_count=100):
        try:
            iporigen = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None
            ipdestino = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst') else None
            if hasattr(pkt,'icmp'):
                print(f"[PING] {iporigen} -> {ipdestino} | tipo {pkt.icmp.type}")
                trafico2.append([iporigen,ipdestino])
        except AttributeError as error:
             print(f"[ERROR] {error}")
             continue
    with open('funcion2.csv',mode ='w',newline = '') as archivo_cvs:
         escritor = csv.writer(archivo_cvs)               
         escritor.writerows(trafico2)
         print(f"Trafico guardado en funcion2.csv")         

def funcion3():
    print("Entrando a funcion 3")
    print ("Detecta sesiones RST-FIN-ACK")
    capture = pyshark.LiveCapture(interface='any', display_filter='tcp')

    finack = False
    resetdetectado = False

    for pkt in capture.sniff_continuously(packet_count=100):
        try:
            if hasattr(pkt, 'tcp'):
                flags = int(pkt.tcp.flags, 16)  

                if flags == 0x11:  # FIN (0x01) + ACK (0x10)
                    print(f"[FIN-ACK] Detectado entre {pkt.ip.src} -> {pkt.ip.dst}")
                    finack = True
                    break

                if flags == 0x04:  # RST
                    print(f"[RST] Detectado entre {pkt.ip.src} -> {pkt.ip.dst}")
                    resetdetectado = True
                    break

        except AttributeError as error:
            print(f"[ERROR] {error}")

    if finack:
        print(" Conexión cerrada por FIN ACK")
    elif resetdetectado:
        print("Conexión cerrada por Reset")
    else:
        print(" No se detectó cierre")    

def login():
    intentos = 0
    while intentos < 3:
        try:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            loginsesion = input("Ingrese su usuario :")
            loginpass = input("Ingrese su contraseña :")
            suma = int(input(f"Verificacion Humana ¿Cuánto es {a} + {b}? "))

            if usersesion == loginsesion and loginpass == passsesion and suma ==(a+b):
                print(" Acceso autorizado ")
                return True
            else:
                intentos +=1
                
                print(f" {intentos}/3 intentos")
        except ValueError:
            intentos +=1
            print(f" {intentos}/3 intentos")
            continue

    print("¡Ah, ah, ah! ¡No dijiste la palabra mágica!\n")
    print('''

   SYSTEM FAILURE
 
        ''')              
    return False

def menu():
     
    while True:
        try:
                    print('''
                Menu
                1) Buscando DNS
                2) Buscando PING
                3) Detecta Fin Sesiones
                4) Salir                                        
                        ''')
                    opcion = int(input("Ingrese su opcion:"))
                    
                    if opcion == 1: funcion1()
                    elif opcion == 2:funcion2()
                    elif opcion == 3 :funcion3()
                    elif opcion == 4 : break
                    else : print(" Reintentar")

        except ValueError:
            print(" Reintentar")
            continue

    
if login():
    menu()

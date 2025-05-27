import pyshark
INTERFAZ = 'any'
from collections import Counter
comunicaciones =[]
capture = pyshark.LiveCapture(interface=INTERFAZ,display_filter='udp')
contador = 0
for packet in capture:
    try:
        if hasattr(packet,'ip') and hasattr(packet,'udp'):
            origen = packet.ip.src
            destino = packet.ip.dst
            port_origen = packet.udp.srcport
            port_destino = packet.udp.dstport
            comunicaciones.append((origen,port_origen,destino,port_destino))
            print (f"Trafico UDP {origen}:{port_origen} -> {destino}:{port_destino}")
            contador +=1
            if contador == 100:
                break
    except AttributeError:
        pass

frecuentes = Counter(comunicaciones)
top5 = frecuentes.most_common(5)
#test rama
print(top5)
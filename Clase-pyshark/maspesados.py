from collections import Counter
import pyshark

interfaz = "any"
num_paquetes = 100
paquetes =[]
captura = pyshark.LiveCapture(interface=interfaz)
for pkt in captura.sniff_continuously(packet_count=num_paquetes):
    try:
        tam = int(pkt.length)
        paquetes.append((tam, pkt))
        print(f"{tam} bytes desde la ip {pkt.ip.src} hacia la ip {pkt.ip.dst} en la capa {pkt.highest_layer} hacia el port {pkt.tcp.port}")   

    except:
        pass

# Mostrar los 5 paquetes más grandes
top_pesados = sorted(paquetes, key=lambda x: x[0], reverse=True)[:5]

print("\n📦 Top 5 paquetes más pesados:")
for tam, pkt in top_pesados:
    try:
        print(f"{tam} bytes desde {pkt.ip.src} → {pkt.ip.dst} en capa {pkt.highest_layer}, puerto {pkt.tcp.port}")
    except:
        print(f"{tam} bytes - información incompleta (posiblemente sin IP o TCP)")


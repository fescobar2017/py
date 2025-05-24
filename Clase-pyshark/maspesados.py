import pyshark

interfaz = "Ethernet 5"
num_paquetes = 100

captura = pyshark.LiveCapture(interface=interfaz)

print("Capturando paquetes...")

paquetes = []
for pkt in captura.sniff_continuously(packet_count=num_paquetes):
    try:
        tam = int(pkt.length)
        paquetes.append((tam, pkt))
        print(f"{tam} bytes")
    except:
        pass

# Mostrar los 2 más grandes
top = sorted(paquetes, key=lambda x: x[0], reverse=True)[:2]

print("\nTop 2 paquetes más grandes:")
for tam, pkt in top:
    print(f"{tam} bytes - {pkt.highest_layer}")
    try:
        print(f"  {pkt.ip.src} → {pkt.ip.dst}")
    except:
        pass
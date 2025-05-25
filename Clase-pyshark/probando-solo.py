import pyshark
INTERFAZ = "any"
num_paquetes = 100
paquetes = []
captura = pyshark.LiveCapture(interface=INTERFAZ)

for pkt in captura.sniff_continuously(packet_count=num_paquetes):
    try:
        tam = int(pkt.length)
        paquetes.append((tam, pkt))
        print(f"{tam} bytes capturado")
    except:
        pass
top_pesados = sorted(paquetes,key=lambda x: x[0],reverse=True)[:5]
print("Los 5 mas pesados son")
posicion = 1
for tam,pkt in top_pesados:
    print(f"{posicion}) {tam} bytes")        
    posicion += 1
        


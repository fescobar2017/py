import pyshark

capture = pyshark.LiveCapture(interface='any', display_filter='tcp')

finack = False
resetdetectado = False

for pkt in capture:
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

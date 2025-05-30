import pyshark
INTERFAZ = 'any'
captura = pyshark.LiveCapture(interface=INTERFAZ, display_filter='tcp.flags.syn == 1')
conexiones = {}
        
for packet in captura.sniff_continuously():
    try:
            ip_origen = packet.ip.src
            ip_destino = packet.ip.dst
            puerto_origen = packet.tcp.srcport
            puerto_destino = packet.tcp.dstport
            clave = (ip_origen, ip_destino, puerto_origen, puerto_destino)
            flags = int(packet.tcp.flags, 16)

            if flags == 0x02:  # SYN
                conexiones[clave] = float(packet.sniff_timestamp)

            elif flags == 0x12:  # SYN-ACK
                clave_respuesta = (ip_destino, ip_origen, puerto_destino, puerto_origen)
                if clave_respuesta in conexiones:
                    tiempo_syn = conexiones.pop(clave_respuesta)
                    tiempo_synack = float(packet.sniff_timestamp)
                    latencia_ms = (tiempo_synack - tiempo_syn) * 1000
                    print(f"{ip_origen}:{puerto_origen} → {ip_destino}:{puerto_destino}")
                    print(f" Latencia estimada: {latencia_ms} ms\n")

    except AttributeError:
        pass


import pyshark
INTERFAZ = 'any'
sesiones =set()
capture = pyshark.LiveCapture(interface=INTERFAZ,display_filter='tcp')

for packet in capture:
    try:
        if hasattr(packet,'tcp') and hasattr(packet,'ip'):
            origen = packet.ip.src
            destino = packet.ip.dst
            sesion = packet.tcp.stream
            pordestino = packet.tcp.dstport
            if sesion not in sesiones:
                print(f"Sesion {sesion}: {origen} → {destino}:{pordestino} ")
                sesiones.add(sesion)

    except AttributeError:
        pass        
        
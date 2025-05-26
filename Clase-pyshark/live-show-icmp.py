import pyshark
INTERFAZ = 'any'
capture = pyshark.LiveCapture(interface=INTERFAZ,display_filter='icmp')
for packet in capture:
    try:
        
        if hasattr(packet,'ip'):
            tipoicmp = int(packet.icmp.type)

            if tipoicmp == 8:
                print(f"Ping detectado hacia {packet.ip.dst}")
            if tipoicmp == 0:
                print(f"Respuesta OK de {packet.ip.src} \n")    
    except AttributeError:
        pass        

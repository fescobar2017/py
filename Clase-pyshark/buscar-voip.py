import pyshark
INTERFAZ = 'any'

captura = pyshark.LiveCapture(interface='any', display_filter='rtp')

for packet in captura:
    try:
        if hasattr(packet,'rtp'):
           rtp = packet.rtp

           print(f" paquete rtp detectado {rtp}")
    except AttributeError:
        pass        



import pyshark
INTERFAZ = 'wlo1'
capture = pyshark.LiveCapture(interface=INTERFAZ)

mac_sospechosas = ['00:00:00:00:00:00','11:11:11:11:11:11','bc:03:58:2a:5c:60']

for packet in capture:
    try:
        mac_origen = packet.eth.src.lower()
        mac_destino = packet.eth.dst.lower()
        
        if mac_origen in mac_sospechosas or mac_destino in mac_sospechosas:
            print(f" Mac Sospechosa detectada en {mac_origen} hacia {mac_destino}")
    except AttributeError:
        pass        
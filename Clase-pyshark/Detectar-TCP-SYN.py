                         
import pyshark

INTERFAZ = 'wlo1'
capture = pyshark.LiveCapture(interface=INTERFAZ)
lista_syn = []
pasadas = 0
for packet in capture:
    try:
        if hasattr(packet, 'ip') and hasattr(packet, 'tcp'):
            pasadas += 1
            if pasadas == 100:
                break
            #print(f"> Capturado: {packet.ip.src} → {packet.ip.dst} | SYN={packet.tcp.flags_syn} ACK={packet.tcp.flags_ack}")
            if packet.tcp.flags_syn == 'True':
                lista_syn.append(packet)
               
                
    except AttributeError:
        pass
for pkt in lista_syn:
    print(f"SYN DETECTADO = {pkt.ip.src} → {pkt.ip.dst}:{pkt.tcp.dstport}")
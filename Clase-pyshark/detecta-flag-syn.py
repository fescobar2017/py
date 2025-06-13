import pyshark

capture = pyshark.LiveCapture(interface='any')

for pkt in capture:
    try:
        if hasattr(pkt,'tcp') and hasattr(pkt.tcp,'flags_fin') and hasattr(pkt.tcp,'flags_ack'):

            if pkt.tcp.flags_fin == '1' and pkt.tcp.flags_ack == '1':
            
                print(f"[FIN-ACK]{pkt.ip.src} {pkt.ip.dst}")
    except AttributeError:
        pass
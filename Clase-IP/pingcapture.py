#Capturar paquetes ICMP y code icmp

import pyshark
capture = pyshark.FileCapture('pesadilla.pcapng',display_filter="icmp")

for pkt in capture:
    try:
        iporigen = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None
        ipdestino = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst') else None

        if hasattr(pkt,'icmp'):
            
            print(f"[PING] {iporigen} -> {ipdestino} | code {pkt.icmp.code} ")


    except AttributeError as error:
        print(f"[ERROR] {error}")    

#Buscando Flags

import pyshark

capture = pyshark.FileCapture('pesadilla.pcapng',display_filter="tcp")

for pkt in capture:
    try:

        iporigen = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None
        ipdestino = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst') else None

        if hasattr(pkt,'tcp') and hasattr(pkt.tcp,'flags'):
            #print(f"[DEBUG] {pkt.tcp.flags}")
            if pkt.tcp.flags == '0x0010':
                print(f"[ACK] {iporigen} -> {ipdestino}")
            if pkt.tcp.flags == '0x0002':
                print(f"[SYN] {iporigen} -> {ipdestino}")
            if pkt.tcp.flags == '0x0001':
                print(f"[FIN] {iporigen} -> {ipdestino}")
            if pkt.tcp.flags == '0x0001' and pkt.tcp.flags =='0x0010' :
                print(f"[FIN-ACK] {iporigen} -> {ipdestino}")

                    
    except AttributeError as error:
        print(f"[ERROR] {error}")    
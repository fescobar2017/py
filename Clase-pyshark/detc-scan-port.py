

import pyshark

capture = pyshark.LiveCapture(interface='any')
scaneados = {}

for pkt in capture:
    try:
        iporigen  = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None
        ipdestino  = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst') else None

        if hasattr(pkt,'tcp') and hasattr(pkt.tcp,'dstport'):
            pordest = pkt.tcp.dstport

            if iporigen not in scaneados:
                scaneados[iporigen] = set()
            
            scaneados[iporigen].add(pordest)

            if len(scaneados[iporigen]) >10:
                print(f"[SCAN] {iporigen} hacia {ipdestino} al port {pordest}")        

    except AttributeError:
        pass
import pyshark
traficorst = {}

capture = pyshark.LiveCapture(interface='wlo1')

for pkt in capture:
    try:

        iporigen = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None
        ipdestino = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst') else None

        if hasattr(pkt,'tcp') and hasattr(pkt.tcp,'dstport'):
            pdestino = pkt.tcp.dstport

            

            if hasattr(pkt,'tcp') and hasattr(pkt.tcp,'flags_rst'):
                if pkt.tcp.flags_rst == '1' :
                    if ipdestino not in traficorst:
                        traficorst[ipdestino] = set()
                    traficorst[ipdestino].add(pdestino)
            
                    if len(traficorst[ipdestino]) > 10 :
                        print(f"[FLAGS-RST] mas de 10 intentos a puerto cerraos {iporigen} -> {ipdestino} {pkt.tcp.flags_rst}")

             
    except AttributeError:
        pass    
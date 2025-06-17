import pyshark

capture = pyshark.LiveCapture(interface='any')
trafico = set()
for pkt in capture:
    try:
        iporigen = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None
        ipdestino = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst') else None
        if hasattr(pkt,'dns') and hasattr(pkt.dns,'qry_name'):
            dns = pkt.dns.qry_name
            
            if dns in trafico: 
                print(f"Este sitio ya fue visitado {dns}  {iporigen} -> {ipdestino}")
        
            else :
                trafico.add(dns)
                
    except AttributeError:
        pass
# "69.163.33.82",
# "87.106.139.101",
# "mixunderax.com",
# "alforcargo.com",
# "181.113.229.139",
# "159.65.241.220"

# Cargar captura y filtrar por TCP o UDP hacia esas IPs

import pyshark
from datetime import datetime

buscaip = ["69.163.33.82","87.106.139.101","181.113.229.139","159.65.241.220"]
buscadns = ["mixunderax.com","alforcargo.com"]

capture = pyshark.FileCapture('pesadilla.pcapng',display_filter="udp or tcp or ip.dst==69.163.33.82 or ip.dst==87.106.139.101 or ip.dst==181.113.229.139 or ip.dst==159.65.241.220")

for pkt in capture:
    try:
        iporigen = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None
        ipdestino = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst') else None
        protocolo = pkt.transport_layer if hasattr(pkt,'transport_layer') else None
        time = float(pkt.sniff_timestamp) if hasattr(pkt, 'sniff_timestamp') else None
        time_fmt = datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S') if time else "Sin timestamp"

        if ipdestino in buscaip:
            print(f"[{protocolo}] {time_fmt} Trafico detectado {iporigen} -> {ipdestino}")

        if hasattr(pkt,'dns') and hasattr(pkt.dns,'qry_name'):
            dns = pkt.dns.qry_name
            if dns in buscadns:
                print(f"[{protocolo}] Trafico detectado {iporigen} -> {dns}")


    except AttributeError as error:
        print(f"[ERROR] {error}")    

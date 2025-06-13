import pyshark

capture = pyshark.LiveCapture('any',display_filter='dns')

for pkt in capture:
    if hasattr(pkt,'dns') and hasattr(pkt.dns,'qry_name'):
        print(f"Dominio detectado {pkt.dns.qry_name}")
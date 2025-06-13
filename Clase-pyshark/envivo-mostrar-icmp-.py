import pyshark
INTERFAZ = 'any'

capture = pyshark.LiveCapture(interface=INTERFAZ, display_filter='icmp')

for pkt in capture:
    try:
        iporigen = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None
        ipdestino = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst') else None
        if hasattr(pkt,'icmp'):
            print(f"[UDP-ICMP] {iporigen} hacia {ipdestino} ")
    except AttributeError as error:
        print(f"[error] con {error}")



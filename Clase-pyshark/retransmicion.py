import pyshark
from collections import Counter

INTERFAZ = 'any'

captura = pyshark.LiveCapture(interface=INTERFAZ, display_filter="tcp.analysis.retransmission")

retransmisiones_por_ip = Counter()

try:
    for packet in captura.sniff_continuously(packet_count=100):  # Puedes quitar el límite si quieres
            print(packet)
            ip_src = packet.ip.src
            ip_dst = packet.ip.dst
            retransmisiones_por_ip[(ip_src, ip_dst)] += 1
            print(f" Retransmisión detectada: {ip_src} → {ip_dst}")
except AttributeError:
        pass

print("IPs con más retransmisiones:")
for (src, dst), count in retransmisiones_por_ip.most_common(5):
    print(f"{src} → {dst} : {count} retransmisiones")

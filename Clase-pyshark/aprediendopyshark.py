import pyshark

INTERFAZ = 'any'  # Cambia a 'eth0', 'wlan0', etc. si lo deseas

print("🔍 Capturando 5 paquetes... mostrando capas por paquete:\n")

# Captura 5 paquetes que cumplan el filtro DNS (rápido y filtrado)
capture = pyshark.LiveCapture(interface=INTERFAZ, display_filter='dns')

# Captura 5 paquetes
for packet in capture.sniff_continuously(packet_count=5):
    print("📦 Nuevo paquete:")
    
    # Muestra todas las capas presentes (ip, udp, dns, etc.)
    for capa in packet.layers:
        print(f"  - Capa: {capa.layer_name}")

    # Si tiene capa DNS y consulta, la imprime
    if hasattr(packet, 'dns') and hasattr(packet.dns, 'qry_name'):
        print(f"🔍 Consulta DNS detectada: {packet.dns.qry_name.lower()}")

    print("-" * 40)

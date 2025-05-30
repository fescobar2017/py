import pyshark
from collections import Counter

INTERFAZ = 'wlo1'  # debe estar en modo monitor
TIEMPO_CAPTURA = 10  # segundos

print(f"🔍 Capturando tráfico Wi-Fi en {INTERFAZ} durante {TIEMPO_CAPTURA} segundos...\n")

# Captura solo tramas Wi-Fi de administración, control y datos
capture = pyshark.LiveCapture(interface=INTERFAZ, display_filter='wlan')

# Contadores
macs_origen = Counter()
macs_destino = Counter()
pares_comunicacion = Counter()

capture.sniff(timeout=TIEMPO_CAPTURA)

for packet in capture:
    try:
        src = packet.wlan.sa  # Source Address
        dst = packet.wlan.da  # Destination Address

        macs_origen[src] += 1
        macs_destino[dst] += 1
        pares_comunicacion[(src, dst)] += 1

    except AttributeError:
        pass

print("📊 Top 5 MACs que más envían tráfico:")
for mac, count in macs_origen.most_common(5):
    print(f"   {mac} → {count} paquetes")

print("\n📡 Top 5 pares de comunicación:")
for (src, dst), count in pares_comunicacion.most_common(5):
    print(f"   {src} → {dst} : {count} paquetes")

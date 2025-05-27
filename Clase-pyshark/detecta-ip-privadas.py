import pyshark
INTERFAZ = 'any'
capture = pyshark.LiveCapture(interface=INTERFAZ)

def es_ip_privada(ip):
    if ip.startswith('10.'):
        return True
    if ip.startswith('192.168.'):
        return True
    if ip.startswith('172.'):
        segundo_octeto = int(ip.split('.')[1])
        if 16 <= segundo_octeto <= 31:
            return True
    return False

for packet in capture:
    try:
        if hasattr(packet, 'ip'):
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst

            if es_ip_privada(src_ip) or es_ip_privada(dst_ip):
                print(f"IP privada detectada:")
                print(f" Origen: {src_ip} → Destino: {dst_ip}")
                print("-" * 60)

    except AttributeError:
        pass
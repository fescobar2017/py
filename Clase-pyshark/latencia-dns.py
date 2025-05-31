import pyshark

INTERFAZ = 'any'
captura = pyshark.LiveCapture(interface=INTERFAZ, display_filter='dns')
consultas_dns = {}


for packet in captura.sniff_continuously(packet_count=50):
    try:
        if not hasattr(packet, 'dns'):
            continue

        dns_layer = packet.dns
        ip_src = packet.ip.src
        ip_dst = packet.ip.dst
        dns_id = dns_layer.id
        timestamp = float(packet.sniff_timestamp)

        qr = getattr(dns_layer, 'flags_response', 'False') == 'True'

        if not qr:
            consultas_dns[dns_id] = timestamp

        else:
            if dns_id in consultas_dns:
                tiempo_inicio = consultas_dns.pop(dns_id)
                tiempo_respuesta = (timestamp - tiempo_inicio) * 1000
                nombre = getattr(dns_layer, 'qry_name', '(sin nombre)')
                print(f"\nDominio: {nombre}")
                print(f"Tiempo de respuesta: {tiempo_respuesta} ms")
                print("-" * 50)

    except AttributeError:
        pass





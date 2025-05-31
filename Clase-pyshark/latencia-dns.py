import pyshark
INTERFAZ = 'any'
captura = pyshark.LiveCapture(interface=INTERFAZ,display_filter='dns')
consultas_dns = {}

for packet in captura.sniff_continuously(packet_count=10):
    try:
        print(packet)
        dns_layer = packet.dns
        ip_src = packet.ip.src
        ip_dst = packet.ip.dst
        dns_id = dns_layer.id
        timestamp = float(packet.sniff_timestamp)

        if dns_layer.qr == 0: # Es una consulta (query)
            clave = (ip_src, ip_dst, dns_id)
            consultas_dns[clave] = timestamp

        elif dns_layer.qr == 1: # Es una respuesta
            clave = (ip_dst, ip_src, dns_id)
            if clave in consultas_dns:
                tiempo_inicio = consultas_dns.pop(clave)
                tiempo_respuesta = (timestamp - tiempo_inicio) * 1000
                nombre = dns_layer.qry_name if hasattr(dns_layer, 'qry_name') else '(sin nombre)'
                print(f"Dominio: {nombre}")
                print(f"Tiempo de respuesta: {tiempo_respuesta} ms")
                print("-" * 50)

    except AttributeError:
        pass


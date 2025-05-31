import pyshark

INTERFAZ = 'any'

print(" Escuchando tráfico TLS...\n")

capture = pyshark.LiveCapture(interface=INTERFAZ, display_filter='ssl.handshake.certificate')

for packet in capture:
    try:
        if hasattr(packet,'tls'):
            print(f"Certificado SSL {packet.tls.handshake_certificate}")
    except AttributeError:
        pass
            
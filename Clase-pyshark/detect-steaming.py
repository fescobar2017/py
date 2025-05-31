#Busca Streaming
import pyshark
INTERFAZ = 'any'

capture = pyshark.LiveCapture(interface=INTERFAZ, display_filter='dns')
streaming = ['youtube','netflix','video']
contador = 0
suma = 0

for packet in capture.sniff_continuously(packet_count=200):
    try:
        if hasattr(packet, 'dns') and hasattr(packet.dns, 'qry_name'):
            query_name = packet.dns.qry_name.lower()
            
            for sitio in streaming:
                if sitio in query_name:
                    print(f" Tráfico hacia streaming detectado {query_name}")
                    tamano = int(packet.length)
                    suma += tamano
                    contador += 1
                
    except AttributeError:
        pass

promedio = suma / contador
print(f"Tráfico total: {suma} bytes en {contador} paquetes detectados de streaming")
print(f"Promedio por paquete: {promedio} bytes")
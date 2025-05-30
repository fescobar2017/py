import pyshark
INTERFAZ = 'any'  
capture = pyshark.LiveCapture(interface=INTERFAZ)
suma = 0
contador = 0

for packet in capture.sniff_continuously(packet_count=100):
    try:
        tamano = int(packet.length)
        suma += tamano
        contador += 1
        print(f"Paquete #{contador}: {tamano} bytes")
    except AttributeError:
        continue

promedio = suma / contador
print ('*'*31)
print(f"*Tamaño promedio: {promedio} bytes*")
print ('*'*31)


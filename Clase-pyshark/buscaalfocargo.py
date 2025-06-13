
import pyshark
import csv
capture = pyshark.FileCapture('pesadilla.pcapng',display_filter='dns')
sitio = ['alforcargo.com']
trafico = []
for pkt in capture:
    if hasattr(pkt,'dns') and hasattr(pkt.dns,'qry_name'):
        if pkt.dns.qry_name in sitio:
            print(F"sitio {pkt.dns.qry_name} detectado")
            trafico.append([pkt.ip.src,pkt.ip.dst,pkt.dns.qry_name])

with open('busqueda.csv',mode='w') as archivo_csv:
    escritor = csv.writer(archivo_csv,delimiter=',')
    escritor.writerow(['IP-Origen','IP-Destino','DNS'])
    escritor.writerows(trafico)    



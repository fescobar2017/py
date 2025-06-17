
# Cargar captura y filtrar por TCP o UDP hacia esas IPs, rambien las Flags, datos deben ser guardado en un csv
# "69.163.33.82",
# "87.106.139.101",
# "mixunderax.com",
# "alforcargo.com",
# "181.113.229.139",
# "159.65.241.220"

import pyshark
import csv
capture = pyshark.FileCapture('pesadilla.pcapng',display_filter='tcp or udp or dns or ip.dst==69.163.33.82 or ip.dst==87.106.139.101 or ip.dst==181.113.229.139 or ip.dst==159.65.241.220' )
trafico = []
buscaip = ['69.163.33.82','87.106.139.101','181.113.229.139','159.65.241.220']
buscadns = ['mixunderax.com','alforcargo.com']

for pkt in capture:
    try:
        
            iporigen = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None
            ipdestino = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst') else None
            bandera = pkt.tcp.flags if hasattr(pkt,'tcp') and hasattr(pkt.tcp,'flags') else None
            protocolo = pkt.transport_layer if hasattr(pkt,'transport_layer') else None

            if ipdestino in buscaip:
                print(f"[{protocolo}][IP] Ip Detectada hacia {ipdestino}")
                trafico.append([iporigen,ipdestino,bandera])

            if hasattr(pkt,'dns') and hasattr(pkt.dns,'qry_name'):
                dns = pkt.dns.qry_name

                if dns in buscadns:                  
                    print(f"[{protocolo}][DNS] visita a {dns} detectado")
                    trafico.append([iporigen,ipdestino,dns])
    except AttributeError as error:
        print(f"[ERROR ATRIBUTO] {error}")
        pass
with open('resultado.csv',mode = 'w',newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(["IP-ORIGEN","IP-DESTINO","DNS/FLAGS"])
    escritor.writerows(trafico)
    print (f"Trafico Guardado en resultado.csv")







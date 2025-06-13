import pyshark
import csv
capture = pyshark.FileCapture('pesadilla.pcapng',display_filter='tcp')
trafico = []
contador = 0
for pkt in capture:
    try:
        iporigen = pkt.ip.src if hasattr(pkt, 'ip') and hasattr(pkt.ip, 'src') else None
        ipdestino = pkt.ip.dst if hasattr(pkt, 'ip') and hasattr(pkt.ip, 'dst') else None
        puertorigen = pkt.tcp.srcport if hasattr(pkt, 'tcp') and hasattr(pkt.tcp, 'srcport') else None
        puertodestino = pkt.tcp.dstport if hasattr(pkt, 'tcp') and hasattr(pkt.tcp, 'dstport') else None
      
        print(f"[TRAFICO] {iporigen}:{puertorigen} -> {ipdestino}:{puertodestino}")   
        trafico.append([iporigen,puertorigen,ipdestino,puertodestino])
      
        contador += 1
        if contador == 100:break

    except AttributeError:
        pass
with open ('juan.csv',mode='w',newline=(''))as archivo:
            escritor =csv.writer(archivo)
            escritor.writerow(['IP-ORIGEN','PORT','IP-DESTINO','PORT'])
            escritor.writerows(trafico)
            print("TRAFICO GUARDADO EN juan.csv")    
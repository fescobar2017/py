# Capturar tráfico DNS y TCP FIN-ACK, datos deben ser guardado en un csv

import pyshark; import csv
capture = pyshark.FileCapture('pesadilla.pcapng',display_filter='dns or tcp.flags==0x011')
trafico = []
for pkt in capture:
    try :

        iporigen = pkt.ip.src if hasattr(pkt,'ip') and hasattr(pkt.ip,'src') else None
        ipdestino = pkt.ip.dst if hasattr(pkt,'ip') and hasattr(pkt.ip,'dst') else None

        if hasattr(pkt,'dns') and hasattr(pkt.dns,'qry_name'):
            dns = pkt.dns.qry_name
            print(f"[DNS]{dns}")
            trafico.append([iporigen,ipdestino,dns])

        if hasattr(pkt,'tcp') and hasattr(pkt.tcp,'flags'):
            bandera = pkt.tcp.flags
            

            if bandera == '0x0011':
                print(f"[FIN-ACK] {iporigen} -> {ipdestino} | Flags {bandera} ")
                trafico.append([iporigen,ipdestino,bandera])


    except AttributeError as error:
        print(f"[ERROR] {error}")
with open('resultado.csv',mode ='w',newline=('')) as archivo_csv:
    escritor =csv.writer(archivo_csv)
    escritor.writerow(['IPORIGEN','IPDESTINO','DNS/FLAG'])
    escritor.writerows(trafico)
    print("Trafico guardo en resultado.csv")            
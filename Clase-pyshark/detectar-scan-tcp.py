import pyshark
INTERFAZ = 'any'
limite = 10
scaneados = {}
capture = pyshark.LiveCapture(interface=INTERFAZ,display_filter='tcp')

for packet in capture:
    try:
        if hasattr(packet,'tcp') and hasattr(packet,'ip'):
            origen = packet.ip.src
            portdest= packet.tcp.dstport

            if origen not in scaneados:
                scaneados[origen]=set()
            scaneados[origen].add(portdest)

            if len(scaneados[origen]) > 20:
                    #print(f" Posible escaneo desde {origen}: {len(scaneados[origen])} puertos distintos")
                    print(f" Escaneo desde {origen} ")
                    print("Puertos:", scaneados[origen])


    except AttributeError:
         pass
   




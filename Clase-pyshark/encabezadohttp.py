import pyshark

capture = pyshark.LiveCapture(interface='any')

for pkt in capture:
    try:
        if hasattr(pkt,'http') and (pkt.http,'host'):
            print(f" Dominio solicitado {pkt.http.host}")

        if hasattr(pkt,'http') and (pkt.http,'user_agent'):
            print(f" Navegador solicitado {pkt.http.user_agent}") 
    except AttributeError:
        pass

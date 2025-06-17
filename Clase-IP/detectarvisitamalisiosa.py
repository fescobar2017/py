import pyshark

malisioso = ['web.facebook.com','x.com','emol.com','api.x.com']

capture = pyshark.LiveCapture(interface='any',display_filter='dns.qry.name')

for pkt in capture:

    try:
        
        if hasattr(pkt,'dns') and hasattr(pkt.dns,'qry_name'):
            consultado = pkt.dns.qry_name
            
            if consultado in malisioso:
                print(f"Sitio {consultado} esta en los malisiosos")


    except AttributeError:
        pass

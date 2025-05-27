import pyshark
INTERFAZ = 'any'

capture = pyshark.LiveCapture(interface=INTERFAZ,display_filter='http')
for packet in capture:
    try:
        if hasattr(packet,'ip') and hasattr(packet,'http'):
            print(f"Host       => {packet.http.host}")
            print(f"User-Agent => {packet.http.user_agent}")
            print(f"Version    => {packet.http.request_version}")
            print("="*120)
    except AttributeError:
        pass
   
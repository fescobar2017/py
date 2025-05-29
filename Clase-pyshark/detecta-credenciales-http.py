import pyshark
INTERFAZ = 'any'
capture = pyshark.LiveCapture(interface=INTERFAZ,display_filter='http')
for packet in capture:
    try:
        texto = str(packet)
        if any(clave in texto.lower() for clave in ['user', 'username', 'admin', 'pass', 'password']):
            print(f"Password detectada:\n{texto}")
            print("=" * 20)
            print("Password detectada")
            print("=" * 20)
            break         
    except Exception:
        pass





import re

def validar_mac(mac):
    patron = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return bool(re.fullmatch(patron, mac.strip()))

def validar_ip(ip):
    patron = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.fullmatch(patron, ip.strip()):
        return False
    partes = ip.strip().split(".")
    return all(0 <= int(bloque) <= 255 for bloque in partes)

def validar_puerto(puerto):
    try:
        p = int(puerto)
        return 1 <= p <= 65535
    except ValueError:
        return False

# Inputs
IpOrigen = input("Ingresa las IPs de origen separadas por comas: ").split(",")
PortOrigen = input("Ingresa los Puertos de origen separados por comas: ").split(",")
IpDestino = input("Ingresa las IPs de destino separadas por comas: ").split(",")
PortDestino = input("Ingresa los Puertos de destino separadas por comas: ").split(",")
MacOrigen = input("Ingresa MACs de origen separadas por comas: ").split(",")
MacDestino = input("Ingresa MACs de destino separadas por comas: ").split(",")

print("\n📡 Resumen de conexiones\n" + "="*80)

for IPO, MO, PO, IPD, MD, PD in zip(IpOrigen, MacOrigen, PortOrigen, IpDestino, MacDestino, PortDestino):
    IPO, MO, PO = IPO.strip(), MO.strip(), PO.strip()
    IPD, MD, PD = IPD.strip(), MD.strip(), PD.strip()

    icono_MO = "✅" if validar_mac(MO) else "❌"
    icono_MD = "✅" if validar_mac(MD) else "❌"
    icono_IPO = "✅" if validar_ip(IPO) else "❌"
    icono_IPD = "✅" if validar_ip(IPD) else "❌"
    icono_PO = "✅" if validar_puerto(PO) else "❌"
    icono_PD = "✅" if validar_puerto(PD) else "❌"

    print(f"""
🔹 Conexión:
├─ Origen   → IP: {IPO:<15} {icono_IPO} | MAC: {MO:<17} {icono_MO} | Puerto: {PO:<5} {icono_PO}
└─ Destino  → IP: {IPD:<15} {icono_IPD} | MAC: {MD:<17} {icono_MD} | Puerto: {PD:<5} {icono_PD}
{"-"*50}
""")

import csv
import re
from collections import Counter

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

# Colores para consola
RED = "\033[91m"
RESET = "\033[0m"

# Rutas
archivo = "/home/francisco/Escritorio/conexiones.csv"
salida_txt = "/home/francisco/Escritorio/reporte_conexiones.txt"

conexiones = []
ips_origen = []

with open(archivo, newline='') as csvfile:
    lector = csv.DictReader(csvfile)
    for fila in lector:
        conexiones.append(fila)
        ips_origen.append(fila['ip_origen'].strip())

repetidas = Counter(ips_origen)

with open(salida_txt, 'w') as salida:
    encabezado = "\n📡 RESUMEN DE CONEXIONES\n" + "=" * 80 + "\n"
    print(encabezado)
    salida.write(encabezado)

    for fila in conexiones:
        IPO = fila['ip_origen'].strip()
        PO = fila['puerto_origen'].strip()
        MO = fila['mac_origen'].strip()
        pais_origen = fila.get('pais_origen', 'Desconocido').strip()

        IPD = fila['ip_destino'].strip()
        PD = fila['puerto_destino'].strip()
        MD = fila['mac_destino'].strip()
        pais_destino = fila.get('pais_destino', 'Desconocido').strip()

        icono_MO = "✅" if validar_mac(MO) else "❌"
        icono_MD = "✅" if validar_mac(MD) else "❌"
        icono_IPO = "✅" if validar_ip(IPO) else "❌"
        icono_IPD = "✅" if validar_ip(IPD) else "❌"
        icono_PO = "✅" if validar_puerto(PO) else "❌"
        icono_PD = "✅" if validar_puerto(PD) else "❌"

        alerta_consola = f"{RED}⚠️ Posible DDoS{RESET}" if repetidas[IPO] > 5 else ""
        alerta_archivo = "⚠️ Posible DDoS" if repetidas[IPO] > 5 else ""

        resumen_consola = f"""
[ Conexión ]
Origen  -> IP: {IPO:<15} {icono_IPO} | MAC: {MO:<17} {icono_MO} | Puerto: {PO:<5} {icono_PO} | País: {pais_origen:<15} {alerta_consola}
Destino -> IP: {IPD:<15} {icono_IPD} | MAC: {MD:<17} {icono_MD} | Puerto: {PD:<5} {icono_PD} | País: {pais_destino}
{"-"*80}
"""
        resumen_txt = resumen_consola.replace(RED, "").replace(RESET, "").replace(alerta_consola, alerta_archivo)

        print(resumen_consola)
        salida.write(resumen_txt)


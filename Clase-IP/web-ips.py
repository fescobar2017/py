import streamlit as st
import pandas as pd
import re
from collections import Counter
import ipaddress

def validar_mac(mac):
    patron = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return bool(re.fullmatch(patron, mac.strip()))

def validar_ip(ip):
    try:
        ipaddress.ip_address(ip.strip())
        return True
    except ValueError:
        return False

def validar_puerto(puerto):
    try:
        p = int(puerto)
        return 1 <= p <= 65535
    except:
        return False

st.title("📡 Analizador de Conexiones por CSV")

archivo = st.file_uploader("Sube un archivo CSV con conexiones", type=["csv"])

if archivo:
    df = pd.read_csv(archivo)

    st.subheader("📊 Vista previa del archivo")
    st.dataframe(df.head())

    conexiones = df.to_dict(orient='records')
    ips_origen = [c['ip_origen'].strip() for c in conexiones]
    repetidas = Counter(ips_origen)

    st.subheader("📄 Resultados")
    for fila in conexiones:
        IPO = fila['ip_origen'].strip()
        PO = fila['puerto_origen']
        MO = fila['mac_origen'].strip()
        pais_origen = fila.get('pais_origen', 'Desconocido').strip()

        IPD = fila['ip_destino'].strip()
        PD = fila['puerto_destino']
        MD = fila['mac_destino'].strip()
        pais_destino = fila.get('pais_destino', 'Desconocido').strip()

        validaciones = {
            "IP Origen": ("✅", "❌")[not validar_ip(IPO)],
            "MAC Origen": ("✅", "❌")[not validar_mac(MO)],
            "Puerto Origen": ("✅", "❌")[not validar_puerto(PO)],
            "IP Destino": ("✅", "❌")[not validar_ip(IPD)],
            "MAC Destino": ("✅", "❌")[not validar_mac(MD)],
            "Puerto Destino": ("✅", "❌")[not validar_puerto(PD)],
        }

        alerta = "⚠️ Posible DDoS" if repetidas[IPO] > 5 else ""

        st.markdown(f"""
        **Conexión**
        - IP Origen: `{IPO}` {validaciones["IP Origen"]}
        - MAC Origen: `{MO}` {validaciones["MAC Origen"]}
        - Puerto Origen: `{PO}` {validaciones["Puerto Origen"]}
        - País Origen: {pais_origen} {'🔴' if alerta else ''}
        - IP Destino: `{IPD}` {validaciones["IP Destino"]}
        - MAC Destino: `{MD}` {validaciones["MAC Destino"]}
        - Puerto Destino: `{PD}` {validaciones["Puerto Destino"]}
        - País Destino: {pais_destino}
        - {alerta}
        ---
        """)

    st.subheader("📈 Estadísticas")
    st.write(f"Total de conexiones: {len(conexiones)}")
    st.write(f"IPs únicas de origen: {len(set(ips_origen))}")
    st.write(f"IPs sospechosas (más de 5 conexiones): {sum(1 for ip in repetidas if repetidas[ip] > 5)}")

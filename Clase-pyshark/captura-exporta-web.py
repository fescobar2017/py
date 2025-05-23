import pyshark
import time
from collections import defaultdict, deque, Counter
from datetime import datetime
import os
import webbrowser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

# --- CONFIGURACIÓN ---
LIMITE_PUERTOS = 10
LIMITE_PAQUETES = 100
UMBRAL_REPETICIONES = 10
VENTANA_SEGUNDOS = 5
MAXIMO_CAPTURA = 500

# --- TRACKERS ---
puertos_por_ip = defaultdict(lambda: deque())
paquetes_por_ip = defaultdict(lambda: deque())
trafico_general = []
repetidos_por_ip = defaultdict(int)

# --- HTML: INICIO DEL INFORME ---
def iniciar_html():
    fecha = datetime.now().strftime('%Y-%m-%d')
    hora = datetime.now().strftime('%H:%M:%S')
    with open('alertas.html', 'w') as f:
        f.write(f"""
<!DOCTYPE html>
<html lang=\"es\">
<head>
    <meta charset=\"UTF-8\">
    <title>Informe de Seguridad de Red</title>
    <style>
        body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; }}
        header {{ background-color: #2c3e50; color: white; padding: 20px; text-align: center; }}
        .logo {{ max-width: 250px; margin-bottom: 10px; }}
        .meta {{ text-align: center; margin-top: 10px; }}
        .meta h1 {{ margin: 10px 0 5px; }}
        .meta h3 {{ margin: 0; }}
        main {{ padding: 20px; }}
        h2 {{ color: #2c3e50; margin-top: 40px; }}
        table {{ border-collapse: collapse; width: 100%; background-color: white; margin-bottom: 30px; }}
        th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
        th {{ background-color: #34495e; color: white; }}
        tr:nth-child(even) {{ background-color: #f9f9f9; }}
        footer {{ text-align: center; padding: 20px; font-size: 0.9em; color: #666; }}
    </style>
</head>
<body>
    <header>
        <img src=\"https://ipleones.cl/wp-content/uploads/2024/10/logo-cacredit.png\" class=\"logo\" alt=\"Logo CACredit\">
        <div class=\"meta\">
            <h1>Informe de Seguridad de Red</h1>
            <h3>Fecha: {fecha} - Hora: {hora}</h3>
            <h3>Autor: Francisco Escobar</h3>
            <h3>Carrera: Ciberseguridad</h3>
        </div>
    </header>
    <main>
        <h2>🔔 Alertas Detectadas</h2>
        <table>
            <tr><th>Fecha/Hora</th><th>Tipo de Alerta</th><th>IP Origen</th><th>Detalle</th></tr>
""")

# --- REGISTRO DE ALERTAS ---
def registrar_alerta_html(mensaje, tipo, ip):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {tipo} | {ip} → {mensaje}")
    fila = f"<tr><td>{timestamp}</td><td>{tipo}</td><td>{ip}</td><td>{mensaje}</td></tr>\n"
    with open('alertas.html', 'a') as f:
        f.write(fila)

# --- ANÁLISIS Y REGISTRO DE TRÁFICO ---
def analizar_paquete(pkt):
    ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if 'ip' in pkt and 'tcp' in pkt:
        ip = pkt.ip.src
        puerto = pkt.tcp.dstport
        timestamp = time.time()
        actividad = puertos_por_ip[ip]
        actividad.append((puerto, timestamp))
        while actividad and timestamp - actividad[0][1] > VENTANA_SEGUNDOS:
            actividad.popleft()
        if len(set(p for p, _ in actividad)) >= LIMITE_PUERTOS:
            registrar_alerta_html(f"Escaneo de puertos hacia {len(set(p for p, _ in actividad))} destinos", "Escaneo", ip)
            actividad.clear()
        trafico = paquetes_por_ip[ip]
        trafico.append(timestamp)
        while trafico and timestamp - trafico[0] > VENTANA_SEGUNDOS:
            trafico.popleft()
        if len(trafico) >= LIMITE_PAQUETES:
            registrar_alerta_html(f"{len(trafico)} paquetes en {VENTANA_SEGUNDOS}s", "Flood TCP", ip)
            trafico.clear()
    src = pkt.ip.src if 'ip' in pkt else 'N/A'
    dst = pkt.ip.dst if 'ip' in pkt else 'N/A'
    proto = pkt.highest_layer
    detalle = ""
    if hasattr(pkt, 'tcp'):
        detalle = f"{pkt.tcp.srcport} → {pkt.tcp.dstport}"
    elif hasattr(pkt, 'udp'):
        detalle = f"{pkt.udp.srcport} → {pkt.udp.dstport}"
    if hasattr(pkt, 'http'):
        detalle += f" | HTTP {getattr(pkt.http, 'host', '')}{getattr(pkt.http, 'request_uri', '')}"
    if hasattr(pkt, 'dns'):
        detalle += f" | DNS {pkt.dns.qry_name}"
    if hasattr(pkt, 'ftp'):
        detalle += f" | FTP {pkt.ftp.request_command} {getattr(pkt.ftp, 'request_arg', '')}"
    if hasattr(pkt, 'tls'):
        detalle += " | TLS Handshake"
        if hasattr(pkt.tls, 'handshake_extensions_server_name'):
            detalle += f" (SNI: {pkt.tls.handshake_extensions_server_name})"

    clave_trafico = (src, dst, proto, detalle)
    repetidos_por_ip[clave_trafico] += 1
    if repetidos_por_ip[clave_trafico] == UMBRAL_REPETICIONES:
        registrar_alerta_html(f"Tráfico repetido hacia {dst} ({proto})", "Repetición Sospechosa", src)

    if 'eicar.org' in detalle.lower():
        registrar_alerta_html(f"Tráfico relacionado con eicar.org detectado: {detalle}", "EICAR", src)

    trafico_general.append({
        'hora': ahora,
        'src': src,
        'dst': dst,
        'proto': proto,
        'detalle': detalle
    })
    print(f"🕒 {ahora} | {src} → {dst} | {proto} | {detalle}")


''' 
Nombre: Francisco Escobar
Evaluación: Programación de Firewall
Tarea: Administrador de firewall
Seccion II Sabados
'''


import re                    # importa la expresiones regulares  
from getpass import getpass  # oculta la contraseña al escribir

#matriz: IP Origen, MAC, IP Destino, Puerto Destino, Protocolo, Permiso 
matriz = [
    ['10.10.10.10', '34:12:34:21:34:23', '192.168.1.1', 55, 'TCP', 'permitir'],
    ['192.168.1.100', 'SS:D2:A3:D2:EE:01', '10.0.0.1', 443, 'TCP', 'denegar'],
    ['172.16.0.1', '12:11:D3:22:34:55', '8.8.8.8', 22, 'UDP', 'permitir'],
    ['192.0.2.25', 'DE:AD:BE:EF:00:01', '8.2.1.1', 8080, 'ALL', 'denegar']
]

# Funcion para validar la ip, separando los octetos para revisar si estan en el rango

def validar_ip(ip):
    partes = ip.split('.')
    if len(partes) != 4:
        return False
    for i, octeto in enumerate(partes):
        if not octeto.isdigit:
            return False
        valor = int(octeto)
        if not 0 <= valor <= 255:
            return False
        if i == 3 and valor == 0:
            return False
    return True

#Funcion Para Validar Mac con patron, revisa si es con (-) cambia a (:)
def validar_mac(mac):
    mac = mac.replace("-", ":")
    return re.match(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$", mac) is not None

#Funcion para Validar el puerto es un numero entre 1 y 65535
def validar_puerto(p):
    return p.isdigit() and 1 <= int(p) <= 65535

#Funcion para validar si el procolo es uno de la lista
def validar_protocolo(proto):
    return proto.upper() in ['TCP', 'UDP', 'ICMP', 'ALL']

'''Funcion para validar si el permiso esta en la lista,
pasa los ingresados a minucuslas para evitar errores de tipeo '''
def validar_permiso(perm):
    return perm.lower() in ['permitir', 'denegar']

#Funcion para Agregar un regla
def agregar_regla():
    while True:
        ip_origen = input("Ingrese IP ORIGEN: ")  #Ingresa la IP de Origen
        if validar_ip(ip_origen): break           #Envia a validar al ip a la funcion ValidarIP   
        print("⚠️ IP ORIGEN inválida. Por favor, ingrese una dirección IP válida (Ej: x.x.x.x).")  # Si Falla se Imprime el IP de Origen Mala
    while True:
        mac = input("Ingrese MAC: ")             #Ingresa la Mac
        if validar_mac(mac): break               #Envia a validar la Mac al la Funcion Validar MAC
        print("⚠️ Dirección MAC no válida. Use el formato hexadecimal separado por dos puntos (ej: 01:23:45:67:89:AB)")   #Si falla el validar imprime Mac Invalida
    while True:
        ip_destino = input("Ingrese IP DESTINO: ") #Ingresa la Ip de Destino
        if validar_ip(ip_destino): break           #Envia la ip destino a la funcion de Validar IP
        print("⚠️ IP DESTINO inválida. Por favor, ingrese una dirección IP válida (Ej: x.x.x.x)")    #Si Falla imprime que la IP Destino no es valida
    while True:                         
        puerto = input("Ingrese PUERTO DESTINO: ")  #Ingresa puerto de Destino
        if validar_puerto(puerto): break            #Envia el puerto a la Funcion de Validar Puerto  
        print("⚠️ Puerto inválido. Por favor, ingrese un número entre 1 y 65535")#Si Falla imprime que puerto no es valido
    while True:
        protocolo = input("Ingrese PROTOCOLO (TCP/UDP/ICMP/ALL): ") #Ingresa el Protocolo
        if validar_protocolo(protocolo): break                      #Envia a validar el protocolo a la funcion de Protocolo
        print("⚠️ Protocolo no válido. Reintente con TCP, UDP, ICMP o ALL") #Si esto Falla imprime protcolo invalido
    while True:
        permiso = input("Ingrese PERMISO (permitir ✅ / denegar ⛔): ") #Ingresa si es permitido o denegado
        if validar_permiso(permiso): break                              #Envia a validar a la funcion Validar permiso
        print("⚠️ Permiso inválido. Por favor, ingrese permitir o denegar") #Si Falla imprime que el permiso no es valido

    regla = [ip_origen, mac, ip_destino, int(puerto), protocolo.upper(), permiso.lower()]  # Forma la regla para insertar
    matriz.append(regla)                                                                   #Inserta la regla en la matriz
    print("Regla agregada correctamente ✅.")                                              # Imprime que la regla fue agregada con exito

def eliminar_regla():                                                                       # Funcion Eliminar Reglas
    mostrar_reglas()                                                                        # Muestra la lista de reglas para poder eliminar   
    idelimina = input("Ingrese ID de la regla a eliminar: ")                                # Ingresa el numero de regla a eliminar
    if idelimina.isdigit() and 0 <= int(idelimina) < len(matriz):                           # Comprueba si lo ingresado es un numero y si esta dentro de la matriz
        matriz.pop(int(idelimina))                                                          # Confirma que la regla fue eliminado
        print("Regla eliminada ✅.")                                                        
    else:
        print("⚠️ ID inválido.")                                                            # de lo contrario imprime que id no es valido

def insertar_regla():                                                                       # Funcion de Inserta la Regla
    idinserta = input("Ingrese posición donde insertar la regla: ")                         # Ingresar la regla que se quiere insertar 
    if not idinserta.isdigit() or not 0 <= int(idinserta) <= len(matriz):                   # Funcion Verifica que el id sea un numero y que este en el rango
        print("⚠️ Posición inválida. Por favor, ingrese un número dentro del rango de la lista de reglas")                                                      # Si Falla indica posicion no valida
        return

    while True:
        ip_origen = input("Ingrese IP ORIGEN: ")                                             # Ingresa la ip de Origen
        if validar_ip(ip_origen): break                                                      # Envia la ip a la funcion de validar IP de origen   
        print("⚠️ IP ORIGEN inválida. Por favor, ingrese una dirección IP válida (Ej: x.x.x.x)") # Si Falla imprime que la ip no es valida

    while True:
        mac = input("Ingrese MAC: ")                                                         #Ingresa la MAC 
        if validar_mac(mac): break                                                           #Envia la Mac a validar en la funcion Validar MAC
        print("⚠️ Dirección MAC no válida. Use el formato hexadecimal separado por dos puntos (ej: 01:23:45:67:89:AB)") #Si la validacion falla imprime Mac No valida

    while True:
        ip_destino = input("Ingrese IP DESTINO: ")                                           #Ingresa la ip de destino
        if validar_ip(ip_destino): break                                                     #Envia la ip a la funcion de Validar IP 
        print("⚠️ IP DESTINO inválida. Por favor, ingrese una dirección IP válida (Ej: x.x.x.x)") #Si falla imprime que la IP no es valida

    while True:
        puerto = input("Ingrese PUERTO DESTINO: ")                                            # Ingresa Puerto Destino
        if validar_puerto(puerto): break                                                      # Envia el puerto a validar a la Funcion validar Puerto
        print("⚠️ Puerto inválido. Por favor, ingrese un número entre 1 y 65535")                                                          # Si falla imprime que el puerto no es valido

    while True:
        protocolo = input("Ingrese PROTOCOLO (TCP/UDP/ICMP/ALL): ")                           #Ingresar los protocolos validos
        if validar_protocolo(protocolo): break                                                #Envia el protocolo a validar a la funcion validar Protocolo
        print("⚠️ Protocolo no válido. Reintente con TCP, UDP, ICMP o ALL")                                                       #Si Falla imprime que el protocolo es invalido

    while True:
        permiso = input("Ingrese PERMISO (permitir ✅ / denegar ⛔): ")                       #Ingresa el permiso 
        if validar_permiso(permiso): break                                                    #Envia el permiso a la funcion de Validar permiso
        print("⚠️ Permiso inválido. Por favor, ingrese permitir o denegar")                                                         #Si Falla imprime que el permiso no es valido

    regla = [ip_origen, mac, ip_destino, int(puerto), protocolo.upper(), permiso.lower()]      #Forma la regla a insertar
    matriz.insert(int(idinserta), regla)                                                       #inserta la regla en la matriz
    print("Regla insertada ✅")                                                                #Imprime la confirmacion

def mostrar_reglas():                                                                                                               #Funcion de Mostrar reglas
    print("=" * 95)                                                                                                                 #Imprime el = *95 para el fronted
    print(f"{'ID':<4} {'IP Origen':<15} {'MAC':<20} {'IP Destino':<15} {'Puerto':<8} {'Protocolo':<10} {'Permiso':<10} Estado")     #Imprime los nombres de columnas  sus espacios
                                                                                                                   # Imprimer el = *95 para la fronted           
    for i, r in enumerate(matriz):                                                                                                  #Ciclo for para leer la matriz
        icono = '✅' if r[5] == 'permitir' else '⛔'                                                                                #Revisa si el icono es Permitir o Bloquear
        print(f"{i:<4} {r[0]:<15} {r[1]:<20} {r[2]:<15} {r[3]:<8} {r[4]:<10} {r[5]:<10} {icono}")                                   #Imprime la lista
        print("-" * 95)                                                                                                             #Imprime el - para serpara la listas

#Autenticacion
PASSWORD = "1234"  #no muy dura pero para el trabajo sirve  
intentos = 3       #Configura el numero de intentos

#para mejorar el Fronted 
print("""
╔════════════════════════════════════════════╗
║           BIENVENIDO AL FIREWALL           ║
║      Sistema de administración de reglas   ║
║                Autor: Francisco            ║
║                    IP LEONES               ║
╚════════════════════════════════════════════╝
""")
#ciclo while de verificacion de password mientras tengamos intentos
while intentos > 0: 

    ingreso = getpass("Ingrese la contraseña para acceder al sistema: ")  #usamos getpass para ocultar lo escrito
    if ingreso == PASSWORD:                  #si el ingreso es igual a la pass rompe el cliclo entrando a la app
        print("✅ Acceso Permitido.\n")
        break
    else:
        intentos -= 1   #si la pass no hace match se resta un intento
        print(f"❌ Contraseña incorrecta. Intentos restantes: {intentos}")

if intentos == 0:   #si se agotan los intentos se terminar el programa
    print(" Demasiados intentos fallidos. Saliendo....")
    exit()

# Menú para elegir las opciones
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar regla")
    print("2. Eliminar regla")
    print("3. Insertar regla en posicion")
    print("4. Listar reglas")
    print("5. Terminar")

    opcion = input("Seleccione una opción: ").strip().lower()

    if opcion == "1":
        agregar_regla()
    elif opcion == "2":
        eliminar_regla()
    elif opcion == "3":
        insertar_regla()
    elif opcion == "4":
        mostrar_reglas()
    elif opcion == "5" or opcion == "terminar":
        print("Programa finalizado.")
        break
    else:
        print("⚠️ Opción no válida")

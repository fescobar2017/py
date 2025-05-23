claves = ["1234", "admin", "qwerty", "secreta123"]
intento = 0

while intento < len(claves):
    print(f"Probando clave: {claves[intento]}")
    if claves[intento] == "secreta123":
        print("¡Clave correcta encontrada! Acceso concedido.")
        break
    intento += 1
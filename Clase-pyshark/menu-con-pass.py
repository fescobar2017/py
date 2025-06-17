import pyshark
usersesion = "a"
passsesion = "b"

def funcion1():
    print("Entrando a funcion 1")

def funcion2():
    print("Entrando a funcion 2")

def funcion3():
    print("Entrando a funcion 3")

def login():
    intentos = 0
    while intentos < 3:
        loginsesion = input("Ingrese su usuario :")
        loginpass = input("Ingrese su contraseña :")

        if usersesion == loginsesion and loginpass == passsesion:
            print(" Acceso autorizado ")
            return True
        else:
            intentos = intentos + 1
            print(f" {intentos}/3 intentos")
            
    print (" Saliendo por intentos fallidos")                
    return False

def menu():
     
    while True:
        try:
                    print('''
                Menu
                1) Funcion 1
                2) Funcion 2
                3) Funcion 3
                4) Salir                                        
                        ''')
                    opcion = int(input("ingrese su opcion:"))
                    
                    if opcion == 1: funcion1()
                    elif opcion == 2:funcion2()
                    elif opcion == 3 :funcion3()
                    elif opcion == 4 : break
                    else : print(" Reintentar")

        except ValueError:
            print(" Reintentar")
            continue

    
if login():
    menu()

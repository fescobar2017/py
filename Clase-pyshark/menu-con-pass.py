import pyshark
import random


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
        try:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            loginsesion = input("Ingrese su usuario :")
            loginpass = input("Ingrese su contraseña :")
            suma = int(input(f"Verificacion Humana ¿Cuánto es {a} + {b}? "))

            if usersesion == loginsesion and loginpass == passsesion and suma ==(a+b):
                print(" Acceso autorizado ")
                return True
            else:
                intentos +=1
                
                print(f" {intentos}/3 intentos")
        except ValueError:
            intentos +=1
            print(f" {intentos}/3 intentos")
            continue

    print("¡Ah, ah, ah! ¡No dijiste la palabra mágica!\n")
    print('''
      ______
   .-'      '-.
  /            \
 |              |
 |,  .-.  .-.  ,|
 | )(_o/  \o_)( |
 |/     /\     \|
 (_     ^^     _)
  \__|IIIIII|__/
   | \IIIIII/ |
   \          /
    `--------`
   SYSTEM FAILURE
 DENNIS NEDRY BLOQUEÓ EL SISTEMA
        ''')              
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
                    opcion = int(input("Ingrese su opcion:"))
                    
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

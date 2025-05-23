import pygame
import random
import math
from pygame import mixer
import os
os.environ['SDL_AUDIODRIVER'] = 'ALSA'

#inicializar pygame
pygame.init()
pygame.mixer.init(44100, -16,2,2048)

#crear la pantalla
pantalla = pygame.display.set_mode((800,600))

#Ttulo e icono
pygame.display.set_caption("Invacion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")

#Musica fondo

mixer.music.load('MusicaFondo.mp3')
mixer.music.play(-1)

#Variables Jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

#Variables enemigo

img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 5

for e in range(cantidad_enemigos):

    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.1)
    enemigo_y_cambio.append(50)

#Variables de la bala

img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio =0.5
bala_visible = False


#Puntajes

puntaje = 1
fuente = pygame.font.Font('freesansbold.ttf',32)
texto_x = 1
texto_y = 1

#Funcion Mostrar puntaje

def mostrar_puntaje(x,y):
    texto = fuente.render(f"Javi Puntos: {puntaje}", True,(255,255,255))
    pantalla.blit(texto, (x, y))


#Funcion Jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

#Funcion Ememigo
def enemigo(x,y, ene):
    pantalla.blit(img_enemigo[ene],(x,y))

#Funcion Disparar bala

def disparar_bala (x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x+16,y+16))


#Funcion detectar coliciones
def hay_colicion(x_1,y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2 ,2) + math.pow(y_2 - y_1 ,2 ))
    if distancia < 27:
        return True
    else:
        return False
     

#LOOP JUEGO
se_ejecuta = True
while se_ejecuta:

    #RGB
    pantalla.blit(fondo,(0,0))


    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

# eventos de presionar flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio -= 0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio += 0.3
            if evento.key == pygame.K_SPACE:
                if bala_visible == False:
                    bala_x = jugador_x
                    disparar_bala(jugador_x, bala_y)        

#evento de soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

#Actualizar posision    
    jugador_x += jugador_x_cambio

#Mantener Margenes jugador
    if jugador_x <= 0:
        jugador_x =0
    elif jugador_x >= 736:
        jugador_x = 736

#Actualizar posision enemigo    
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]

#Mantener Margenes enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.1
            enemigo_y[e] += enemigo_y_cambio[e]
    #Colicion
        colicion = hay_colicion(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colicion:
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(50,200)
        enemigo(enemigo_x[e],enemigo_y[e], e)

#Movimiento Bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible == True:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio


    jugador(jugador_x,jugador_y)
    mostrar_puntaje(texto_x,texto_y)    

#Actualizar
    pygame.display.update()


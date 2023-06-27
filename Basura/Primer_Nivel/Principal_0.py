import pygame 
from Niveles.Personaje import *


def mover_personaje(rectangulo_personaje: pygame.Rect, velocidad):
    rectangulo_personaje.x += velocidad

def animar_personaje(pantalla, rectangulo_personaje, accion_personaje):
    global contador_pasos
    largo = len(accion_personaje)
    if contador_pasos >= largo:
        contador_pasos = 0
        
    pantalla.blit(accion_personaje[contador_pasos],rectangulo_personaje)
    contador_pasos += 1


def actualizar_pantalla(pantalla, que_hace, rectangulo_personaje, velocidad,):
    
    match que_hace:
        case "Derecha":
            animar_personaje(pantalla, rectangulo_personaje,personaje_camina)
            mover_personaje(rectangulo_personaje,velocidad)
        case "Quieto":
            animar_personaje(pantalla,rectangulo_personaje,personaje_quieto)


W,H = 1080,900
FPS = 18

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W,H))


#FONDO

fondo = pygame.image.load("Recursos/Fondo/1er Nivel.jpg")
fondo = pygame.transform.scale(fondo,(W,H))

PANTALLA.blit(fondo,(0,0))

# PERSONAJE

rectangulo_personaje = personaje_quieto[0].get_rect()
rectangulo_personaje.x = W/2 - 550
rectangulo_personaje.y = 750
rectangulo_personaje.width = 200
rectangulo_personaje.height = 500


# x_inicial = W/2 - 400

# y_inicial = 1900

contador_pasos = 0

velocidad = 10

# rectangulo_personaje = personaje_quieto[0].get_rect()
# # rectangulo_personaje_x = x_inicial
# # rectangulo_personaje_y = y_inicial

posicion_actual_x = 0

que_hace = "Quieto"

while True:
    RELOJ.tick(FPS) 
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            break
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and rectangulo_personaje.x < (W+5) - velocidad - rectangulo_personaje.width:
        que_hace = "Derecha"
    else:
        que_hace = "Quieto"
    
    PANTALLA.blit(fondo,(0,0))

    actualizar_pantalla(PANTALLA, que_hace, rectangulo_personaje,velocidad)    
    
    pygame.display.update()
import pygame 
from Niveles.Personaje import *
from Clase.Modo import *
from Enemigo import *
from time import sleep
W,H = 1500,900
FPS = 18
########################################################################################################
def aplicar_gravedad(pantalla,  personaje_animacion, rectangulo_personaje: pygame.Rect,piso: pygame.Rect):
    global desplazamiento_y,esta_saltando
    
    if esta_saltando:
        animar_personaje (pantalla, rectangulo_personaje, personaje_animacion)

    rectangulo_personaje.y += desplazamiento_y
    if desplazamiento_y + gravedad < limite_velocidad_caida:
        desplazamiento_y += gravedad
    if rectangulo_personaje.colliderect(piso):
        esta_saltando = False
        desplazamiento_y = 0
        rectangulo_personaje.bottom = piso.top


def mover_personaje(rectangulo_personaje: pygame.Rect, velocidad):
    rectangulo_personaje.x += velocidad

def animar_personaje(pantalla, rectangulo_personaje, accion_personaje):
    global contador_pasos
    largo = len(accion_personaje)
    if contador_pasos >= largo:
        contador_pasos = 0
        
    pantalla.blit(accion_personaje[contador_pasos], rectangulo_personaje)
    contador_pasos += 1
    
    
def realizar_accion_personaje(pantalla, accion_personaje, rectangulo_personaje, velocidad):
    global desplazamiento_y,esta_saltando
    
    match accion_personaje:
        case "Derecha":
            animar_personaje(pantalla, rectangulo_personaje,personaje_camina)
            mover_personaje(rectangulo_personaje,velocidad)
        case "Izquierda":
            animar_personaje(pantalla, rectangulo_personaje,personaje_camina_izquierda)
            mover_personaje(rectangulo_personaje,velocidad*-1)
        case "Salta":
            if not esta_saltando:
                esta_saltando = True
                desplazamiento_y = potencia_salto
                animar_personaje(pantalla,rectangulo_personaje,personaje_salta)
        case "Quieto":
            animar_personaje(pantalla,rectangulo_personaje,personaje_quieto)
        case "Daño":
            animar_personaje(pantalla,rectangulo_personaje,personaje_daño)
    aplicar_gravedad(pantalla,personaje_salta,rectangulo_personaje,piso)
    
    
########################################################################################################   
def realizar_accion_enemigo(pantalla, accion_enemigo, rectangulo_enemigo, velocidad):
    
    match accion_enemigo:
        case "Quieto":
            animar_personaje(pantalla, rectangulo_enemigo,personaje_enemigo_quieto)
        case "Derecha":
            animar_personaje(pantalla, rectangulo_enemigo,personaje_enemigo_camina)
            mover_personaje(rectangulo_enemigo,velocidad)
        case "Izquierda":
            animar_personaje(pantalla, rectangulo_enemigo,personaje_enemigo_camina_izquierda)
            mover_personaje(rectangulo_enemigo,velocidad*-1)
        case "Ataque":
            animar_personaje(pantalla, rectangulo_enemigo, personaje_enemigo_ataca)
        case "Kunai":
            animar_personaje(pantalla, rectangulo_kunai, personaje_kunai)
            mover_personaje(rectangulo_kunai,velocidad)



def desaparecer_kunai(rectangulo_kunai):
    rectangulo_kunai.x = rectangulo_enemigo.x 
    rectangulo_kunai.y = rectangulo_enemigo.y

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W,H))
#FONDO

fondo = pygame.image.load("Recursos/Fondo/1er Nivel.jpg")
fondo = pygame.transform.scale(fondo,(W,H))


########################################################################################################
# PERSONAJE
rectangulo_personaje = personaje_quieto[0].get_rect()
rectangulo_personaje.x = W/2 - 500
rectangulo_personaje.y = 800

contador_pasos = 0

velocidad = 5

posicion_actual_x = 0

lista_animaciones = [personaje_quieto, personaje_camina, 
                    personaje_camina_izquierda, personaje_corre, personaje_corre_izquierda,
                    personaje_daño]
########################################################################################################

########################################################################################################
#enemigo

rectangulo_enemigo = personaje_enemigo_camina[0].get_rect()
rectangulo_enemigo.x = random.randrange(0,W,50)
rectangulo_enemigo.y = 800
rectangulo_enemigo.width = 500
rectangulo_enemigo.height = 80
lista_animaciones_enemigo = [personaje_enemigo_quieto,personaje_enemigo_camina, 
                            personaje_enemigo_camina_izquierda, personaje_enemigo_ataca]

rectangulo_kunai = personaje_kunai[0].get_rect()
rectangulo_kunai.x = rectangulo_enemigo.colliderect(rectangulo_personaje)
rectangulo_kunai.y = rectangulo_enemigo.y
rectangulo_kunai.width = 10
rectangulo_kunai.height = 15
lista_animaciones_kunai = [personaje_kunai]
########################################################################################################

reescalar_imagenes(lista_animaciones_enemigo, 65, 70)
reescalar_imagenes(lista_animaciones, 80, 75)
reescalar_imagenes(lista_animaciones_kunai, 15, 40)
gravedad = 1
potencia_salto = -20
limite_velocidad_caida = 20
esta_saltando = False
desplazamiento_y = 0

########################################################################################################
#SUPERFICIE
piso = pygame.Rect(0,0,W,20)
piso.top = rectangulo_personaje.bottom
########################################################################################################

accion_personaje = "Quieto"
accion_enemigo = "Quieto"
ataque = 0

while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            break
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT] and rectangulo_personaje.x < (W+5) - velocidad - rectangulo_personaje.width:
        accion_personaje = "Derecha"
    elif keys[pygame.K_LEFT] and rectangulo_personaje.x > 0 - velocidad:
        accion_personaje = "Izquierda"
    elif keys[pygame.K_LSHIFT] and rectangulo_personaje.x < (W+5) - velocidad - rectangulo_personaje.width:
        accion_personaje = "Corre"
    elif keys[pygame.K_UP]:
        accion_personaje = "Salta" 
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()
    else:
        accion_personaje = "Quieto"
    
    PANTALLA.blit(fondo,(0,0))

    if rectangulo_enemigo.x < (W+5):
        accion_enemigo = "Derecha"
    elif rectangulo_enemigo.x > (W):
            rectangulo_enemigo.x = 0

    if  ataque == 0 and rectangulo_enemigo.colliderect(rectangulo_personaje):
        accion_enemigo = "Ataque"
        realizar_accion_enemigo(PANTALLA, accion_enemigo,rectangulo_enemigo, 5)
        ataque = 1 
        
    if ataque == 1:
        accion_enemigo = "Kunai"
        if rectangulo_kunai.colliderect(rectangulo_personaje):
            desaparecer_kunai(rectangulo_kunai)
            accion_personaje = "Daño"
        elif rectangulo_kunai.x > W:
            desaparecer_kunai(rectangulo_kunai)
        ataque = 0
        
    realizar_accion_enemigo(PANTALLA, accion_enemigo,rectangulo_enemigo, 5)       
    realizar_accion_personaje(PANTALLA, accion_personaje, rectangulo_personaje,velocidad)

    pygame.draw.rect(PANTALLA, "Red", rectangulo_personaje,2)
    pygame.draw.rect(PANTALLA, "Blue", piso,2)
    pygame.draw.rect(PANTALLA, "Green",rectangulo_enemigo,5)
    pygame.draw.rect(PANTALLA, "Red",rectangulo_kunai,5)
    
    pygame.display.update()
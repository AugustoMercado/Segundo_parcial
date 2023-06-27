import pygame
from Niveles.Personaje import *
from Clase.Modo import *
from Enemigo import *


W, H = 1500, 900
FPS = 18


#############################################################################################
def aplicar_gravedad(pantalla, personaje_animacion, rectangulo_personaje: pygame.Rect, piso: pygame.Rect):
    global desplazamiento_y, esta_saltando

    if esta_saltando:
        animar_personaje(pantalla, rectangulo_personaje, personaje_animacion)

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
    global desplazamiento_y, esta_saltando

    match accion_personaje:
        case "Derecha":
            animar_personaje(pantalla, rectangulo_personaje, personaje_camina)
            mover_personaje(rectangulo_personaje, velocidad)
        case "Izquierda":
            animar_personaje(pantalla, rectangulo_personaje, personaje_camina_izquierda)
            mover_personaje(rectangulo_personaje, velocidad * -1)
        case "Ataque":
            animar_personaje(pantalla, rectangulo_personaje, personaje_ataque)
        case "Salta":
            if not esta_saltando:
                esta_saltando = True
                desplazamiento_y = potencia_salto
                animar_personaje(pantalla, rectangulo_personaje, personaje_salta)
        case "Quieto":
            animar_personaje(pantalla, rectangulo_personaje, personaje_quieto)
        case "Daño":
            animar_personaje(pantalla, rectangulo_personaje, personaje_daño)
    aplicar_gravedad(pantalla, personaje_salta, rectangulo_personaje, piso)


####################################################################################################
def realizar_accion_enemigo(pantalla, accion_enemigo, rectangulo_enemigo, muerto):
    match accion_enemigo:
        case "Quieto derecha":
            if muerto != 1:
                animar_personaje(pantalla, rectangulo_enemigo, personaje_enemigo_quieto)
        case "Quieto izquierda":
            if muerto != 1:
                animar_personaje(pantalla,rectangulo_enemigo,personaje_enemigo_quieto_izquierda)
        case "Ataque derecha":
            if muerto != 1:
                animar_personaje(pantalla, rectangulo_enemigo, personaje_enemigo_ataca)
        case "Ataque izquierda":
            if muerto != 1:
                animar_personaje(pantalla, rectangulo_enemigo, personaje_enemigo_ataca_izquierda)
        case "Muerte":
            if muerto == 1:
                animar_personaje(pantalla, rectangulo_enemigo, personaje_muerte)
            


def desaparecer_kunai(rectangulo_kunai):
    rectangulo_kunai.x = rectangulo_enemigo.x
    rectangulo_kunai.y = rectangulo_enemigo.y

def desaparecer_flecha(personaje_flecha):
    personaje_flecha.x = rectangulo_personaje.x
    personaje_flecha.y = rectangulo_personaje.y



pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))
# FONDO

fondo = pygame.image.load("Recursos/Fondo/1er Nivel.jpg")
fondo = pygame.transform.scale(fondo, (W, H))
###########################
# Tiempo
time = 5
banner_time = pygame.image.load("Recursos/Tiempo/1.png")
# Fuente

fuente = pygame.font.SysFont("ALGERIAN", 50)

#Musica
pygame.mixer.init()
sonido_recolectar = pygame.mixer.Sound("LAST CHANCE.mp3")
sonido_recolectar.set_volume(0.5)
sonido_recolectar.play()


########################################################################################################
# PERSONAJE
rectangulo_personaje = personaje_camina[0].get_rect()
rectangulo_personaje.x = W / 2 - 500
rectangulo_personaje.y = 800

personaje_vida = pygame.image.load("Recursos/VIDA/0.png")

# rectangulo_vida = personaje_vida[0].get_rect()

contador_pasos = 0

velocidad = 5

posicion_actual_x = 0

lista_animaciones = [
    personaje_quieto,
    personaje_camina,
    personaje_camina_izquierda,
    personaje_corre,
    personaje_corre_izquierda,
    personaje_daño,
    personaje_ataque
]

flecha = (pygame.image.load("Recursos/Personaje/Ataque/Flecha/0.png"))
personaje_flecha = (pygame.transform.scale(flecha, (55, 25))).get_rect()
personaje_flecha.x = rectangulo_personaje.x
personaje_flecha.y = rectangulo_personaje.y
########################################################################################################

########################################################################################################
# enemigo

rectangulo_enemigo = personaje_enemigo_quieto[0].get_rect()
rectangulo_enemigo.x = random.randrange(0, W, 50)
rectangulo_enemigo.y = 800
rectangulo_enemigo.width = 500
rectangulo_enemigo.height = 80
lista_animaciones_enemigo = [
    personaje_enemigo_quieto,
    personaje_enemigo_quieto_izquierda,
    personaje_enemigo_ataca,
    personaje_enemigo_ataca_izquierda,
    personaje_muerte
]

rectangulo_kunai = personaje_kunai[0].get_rect()
rectangulo_kunai.x = rectangulo_enemigo.x + 20
rectangulo_kunai.y = 900
rectangulo_kunai.width = 10
rectangulo_kunai.height = 15
lista_animaciones_kunai = [personaje_kunai]
########################################################################################################
##############################################################################



#################################################################################

reescalar_imagenes(lista_animaciones_enemigo, 65, 70)
reescalar_imagenes(lista_animaciones, 80, 75)
reescalar_imagenes(lista_animaciones_kunai, 15, 40)

##########################################################################
#salto
gravedad = 1
potencia_salto = -15
limite_velocidad_caida = 20
esta_saltando = False
desplazamiento_y = 0

########################################################################################################
# SUPERFICIE
piso = pygame.Rect(0, 0, W, 20)
piso.top = rectangulo_personaje.bottom
########################################################################################################

muerte = 0
contador_daño = 0
ataque_personaje = 0
ataque_enemigo = 0
flag = True
time = 60
accion_enemigo = "Quieto"
velocidad_kunai = 10
while flag:
    
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            break
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_RIGHT]
        and rectangulo_personaje.x < (W + 5) - velocidad - rectangulo_personaje.width):
        accion_personaje = "Derecha"
    elif keys[pygame.K_LEFT] and rectangulo_personaje.x > 0 - velocidad:
        accion_personaje = "Izquierda"
    elif (keys[pygame.K_LSHIFT]
        and rectangulo_personaje.x < (W + 5) - velocidad - rectangulo_personaje.width):
        accion_personaje = "Corre"
    elif keys[pygame.K_UP]:
        accion_personaje = "Salta"
    elif keys[pygame.K_k]:
        accion_personaje = "Ataque"
        ataque_personaje = 1
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()
    else:
        accion_personaje = "Quieto"

    PANTALLA.blit(fondo, (0, 0))

    vida_1 = PANTALLA.blit(pygame.transform.scale(personaje_vida, (80, 80)), (80, 10))
    
    if muerte == 0:
        if rectangulo_enemigo.x < rectangulo_personaje.x:
            if rectangulo_enemigo.colliderect(rectangulo_personaje):
                    accion_enemigo = "Ataque derecha"
                    ataque_enemigo = 1
                    velocidad_kunai += 10
            else:
                accion_enemigo = "Quieto"
        elif rectangulo_enemigo.x > rectangulo_personaje.x:
            if rectangulo_enemigo.colliderect(rectangulo_personaje):
                accion_enemigo = "Ataque izquierda"
                ataque_enemigo = 1
                velocidad_kunai *= -1
            else:
                accion_enemigo = "Quieto izquierda"
        realizar_accion_enemigo(PANTALLA, accion_enemigo, rectangulo_enemigo,0)
        
    if ataque_enemigo == 1:
            animar_personaje(PANTALLA, rectangulo_kunai, personaje_kunai)
            mover_personaje(rectangulo_kunai, velocidad_kunai)
            if rectangulo_kunai.colliderect(rectangulo_personaje):
                desaparecer_kunai(rectangulo_kunai)
                accion_personaje = "Daño"
                ataque_enemigo = 0
            elif rectangulo_kunai.x > W:
                desaparecer_kunai(rectangulo_kunai)
                ataque_enemigo = 0
                        
    realizar_accion_personaje(PANTALLA, accion_personaje, rectangulo_personaje, velocidad)

    if ataque_personaje == 1 and personaje_flecha.x < W and muerte == 0:
        mover_personaje (personaje_flecha, 50)
        if personaje_flecha.x == (W):
            desaparecer_flecha(personaje_flecha)
        elif personaje_flecha.colliderect(rectangulo_enemigo):
            ataque_personaje = 0
            accion_enemigo = "Muerte"
            desaparecer_flecha(personaje_flecha)
            contador_daño += 1
            if contador_daño == 2:
                muerte = 1
                realizar_accion_enemigo(PANTALLA, accion_enemigo, rectangulo_enemigo,1)
                    



    logo_tiempo = PANTALLA.blit(pygame.transform.scale(banner_time, (80, 50)), (W / 2 - 30, 10))
    pygame.draw.rect(PANTALLA, "Green", rectangulo_enemigo,5)
    pygame.draw.rect(PANTALLA, "Red", personaje_flecha,5)
    pygame.draw.rect(PANTALLA, "Red", rectangulo_personaje,5)
    
    
    # if time > 0:
    #     time -= 1
    # else:
    #     time = 0
    #     pygame.quit()
    #     flag = False

    tiempo = fuente.render(":{0}".format(time), True, [255, 255, 255])
    PANTALLA.blit(tiempo, (W / 2 + 50, 10))

    pygame.display.update()

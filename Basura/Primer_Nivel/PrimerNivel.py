import pygame
import random
from Niveles.Personaje import *
from Enemigo import *
from Moneda import *
from time import sleep
import turtle

W, H = 1500, 900
FPS = 30


#############################################################################################
def obtener_rectangulos(principal: pygame.Rect):
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 6)

    return diccionario


def aplicar_gravedad(pantalla, personaje_animacion, rectangulo_personaje: pygame.Rect, lados_pisos: list):
    global desplazamiento_y, esta_saltando

    if esta_saltando:
        animar(pantalla, rectangulo_personaje["main"], personaje_animacion)

    for lado in rectangulo_personaje:
        rectangulo_personaje[lado].y += desplazamiento_y

    if desplazamiento_y + gravedad < limite_velocidad_caida:
        desplazamiento_y += gravedad

    for plataforma in lados_pisos:
        if rectangulo_personaje["bottom"].colliderect(plataforma["top"]):
            esta_saltando = False
            desplazamiento_y = 0
            rectangulo_personaje["main"].bottom = plataforma["main"].top + 5
            break
        # agregar parte si choca con alguna otra parte

        else:
            esta_saltando = True


def mover_personaje(rectangulo_personaje: pygame.Rect, velocidad):
    for lado in rectangulo_personaje:
        rectangulo_personaje[lado].x += velocidad


def mover(rectangulo_personaje: pygame.Rect, velocidad):
    rectangulo_personaje.x += velocidad


def animar(pantalla, rectangulo_personaje, accion_personaje):
    
    global contador_pasos
    largo = len(accion_personaje)
    if contador_pasos >= largo:
        contador_pasos = 0
    
    pantalla.blit(accion_personaje[contador_pasos], rectangulo_personaje)
    contador_pasos += 1


def animar_objeto(pantalla, rectangulo_personaje, accion_personaje):
    global contador_pasos_objeto
    largo = len(accion_personaje)
    if contador_pasos_objeto >= largo:
        contador_pasos_objeto = 0
        
    pantalla.blit(accion_personaje[contador_pasos_objeto], rectangulo_personaje)
    contador_pasos_objeto += 1



def realizar_accion_personaje(pantalla, accion_personaje, lados_personaje, velocidad, plataformas):
    global desplazamiento_y, esta_saltando

    pantalla.blit(fondo, (0, 0))
    pantalla.blit(plataforma, (rectangulo_plataforma.x, rectangulo_plataforma.y))
    
    match accion_personaje:
        case "Derecha":
            animar(pantalla, lados_personaje["main"], personaje_camina)
            mover_personaje(lados_personaje, velocidad)
        case "Izquierda":
            animar(pantalla, lados_personaje["main"], personaje_camina_izquierda)
            mover_personaje(lados_personaje, velocidad * -1)
        case "Ataque":
            if not esta_saltando:
                animar(pantalla, lados_personaje["main"], personaje_ataque)
        case "Ataque izquierda":
            if not esta_saltando:
                animar(pantalla, lados_personaje["main"], personaje_ataque_izquierda)
        case "Salta":
            if not esta_saltando:
                esta_saltando = True
                desplazamiento_y = potencia_salto
                animar(pantalla, lados_personaje["main"], personaje_salta)
                mover_personaje(lados_personaje, velocidad)
        case "Quieto":
            if not esta_saltando:
                animar(pantalla, lados_personaje["main"], personaje_quieto)
        case "Quieto izquierda":
            if not esta_saltando:
                animar(pantalla, lados_personaje["main"], personaje_quieto_izquierda)
        case "Daño":
            if not esta_saltando:
                animar(pantalla, lados_personaje["main"], personaje_daño)
    aplicar_gravedad(pantalla, personaje_salta, lados_personaje, plataformas)

    
def realizar_accion_enemigo(pantalla, accion_enemigo, lados_enemigo):
    
    match accion_enemigo:
        case "Quieto derecha":
                animar(pantalla, lados_enemigo["main"], personaje_enemigo_quieto)
        case "Quieto izquierda":
                animar(pantalla, lados_enemigo["main"], personaje_enemigo_quieto_izquierda)
        case "Ataque derecha":
                animar(pantalla, lados_enemigo["main"], personaje_enemigo_ataca)
        case "Ataque izquierda":
                animar(pantalla, lados_enemigo["main"], personaje_enemigo_ataca_izquierda)
        case "Muerte":
                animar(pantalla, lados_enemigo["main"], personaje_muerte)    

    

def desaparecer_kunai(rectangulo_kunai):
    rectangulo_kunai.x = rectangulo_enemigo.x
    rectangulo_kunai.y = rectangulo_enemigo.y


def desaparecer_flecha(personaje_flecha, posicion_actual_x,  posicion_actual_y):
    personaje_flecha.x = posicion_actual_x
    personaje_flecha.y = posicion_actual_y + 10


pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))

# FONDO
fondo = pygame.image.load("Recursos/Fondo/1er Nivel.jpg")
fondo = pygame.transform.scale(fondo, (W, H))

# Tiempo
time = 5
banner_time = pygame.image.load("Recursos/Tiempo/1.png")

# Fuente
fuente = pygame.font.SysFont("ALGERIAN", 50)

# Musica
pygame.mixer.init()
musica_ambiente = pygame.mixer.Sound("Joyous Geisha.mp3")
musica_ambiente.set_volume(0.09)
musica_ambiente.play()


########################################################################################################
# PERSONAJE
rectangulo_personaje = personaje_quieto_izquierda[0].get_rect()
rectangulo_personaje.x = W / 2 - 500
rectangulo_personaje.y = 790

lados_personaje = obtener_rectangulos(rectangulo_personaje)

personaje_vida = pygame.image.load("Recursos/VIDA/0.png")
personaje_menos_una_vida = pygame.image.load("Recursos/VIDA/cruz rojaa.png")
contador_pasos = 0

posicion_actual_y = 0
posicion_actual_x = 0
velocidad = 5

# lista_animaciones = [
#     personaje_quieto,
#     personaje_quieto_izquierda,
#     personaje_camina,
#     personaje_camina_izquierda,
#     personaje_daño,
#     personaje_ataque,
#     personaje_ataque_izquierda,
# ]

lista_animaciones = [
    personaje_camina,
    personaje_camina_izquierda,
    personaje_ataque,
    personaje_ataque_izquierda,
    personaje_daño,
    personaje_salta
]

flecha = pygame.image.load("Recursos/Personaje/Ataque/Flecha/0.png")
personaje_flecha = (pygame.transform.scale(flecha, (55, 25))).get_rect()
personaje_flecha.x = rectangulo_personaje.x
personaje_flecha.y = rectangulo_personaje.y + 10
lista_flecha = [flecha]
flecha_atras = girar_imagen(lista_flecha, True, False)

########################################################################################################

########################################################################################################
# enemigo

rectangulo_enemigo = personaje_enemigo_quieto[0].get_rect()
rectangulo_enemigo.x = W / 2 + 600
rectangulo_enemigo.y = 810

# hacer un rectangulo de vision y adentro un rectangulo del personaje.
lados_enemigo = obtener_rectangulos(rectangulo_enemigo)

rectangulo_vision = personaje_enemigo_quieto[0].get_rect()
rectangulo_vision.x = rectangulo_enemigo.x - 250
rectangulo_vision.y = 800
rectangulo_vision.width = 600
rectangulo_vision.height = 99


lista_animaciones_enemigo = [
    personaje_enemigo_quieto,
    personaje_enemigo_quieto_izquierda,
    personaje_enemigo_ataca,
    personaje_enemigo_ataca_izquierda,
    personaje_muerte,
]

rectangulo_kunai = personaje_kunai[0].get_rect()
rectangulo_kunai.x = rectangulo_enemigo.x + 20
rectangulo_kunai.y = 900
rectangulo_kunai.width = 10
rectangulo_kunai.height = 15
lista_animaciones_kunai = [personaje_kunai]


########################################################################################################

# item_especial = pygame.image.load("Recursos/item_especial/0.png")

# recntarectangulo_item_especial = item_especial[0].get_rect()
# recntarectangulo_item_especial.x=  lados_plataforma
# recntarectangulo_item_especial.y = lados_plataforma["top"]

contador_pasos_objeto = 0
lista_animaciones_objetos = [item_moneda, obtener_item_moneda]

#################################################################################
reescalar_imagenes(lista_animaciones_enemigo, 60, 70)
reescalar_imagenes(lista_animaciones, 80, 90)
reescalar_imagenes(lista_animaciones_kunai, 15, 40)
reescalar_imagenes(lista_animaciones_objetos, 20, 40)
#################################################################################
# salto
gravedad = 1
potencia_salto = -15
limite_velocidad_caida = 15
esta_saltando = False
desplazamiento_y = 0

########################################################################################################
# SUPERFICIE

piso = pygame.image.load("Recursos/Plataforma/0.png")
piso = pygame.transform.scale(piso, (350, 50))
rectangulo_piso = piso.get_rect()
rectangulo_piso.top = 880
rectangulo_piso.x = 0

lados_piso = obtener_rectangulos(rectangulo_piso)

########################################################################################################


segundo_piso =  pygame.image.load("Recursos/Plataforma/0.png")
segundo_piso = pygame.transform.scale(segundo_piso, (850, 50))
rectangulo_segundo_piso = segundo_piso.get_rect()
rectangulo_segundo_piso.x = 790
rectangulo_segundo_piso.top = 880
lados_segundo_piso = obtener_rectangulos(rectangulo_segundo_piso)

########################################################################################################

plataforma = pygame.image.load("Recursos/Plataforma/0.png")
plataforma = pygame.transform.scale(plataforma, (350, 20))  
rectangulo_plataforma = plataforma.get_rect()
rectangulo_plataforma.x = 420
rectangulo_plataforma.y = 780

lados_plataforma = obtener_rectangulos(rectangulo_plataforma)

########################################################################################################


lista_plataformas = [lados_piso, lados_plataforma, lados_segundo_piso]


########################################################################################################


item_especial = pygame.image.load("Recursos/item_especial/0.png")
item_especial = pygame.transform.scale(item_especial, (20, 20))
rectangulo_item = item_especial.get_rect()
rectangulo_item.x = rectangulo_plataforma.x + 50
rectangulo_item.y = rectangulo_plataforma.y - 50
diccionario_item = {}
diccionario_item["superficie"] = item_especial
diccionario_item["rectangulo"] = rectangulo_item


time = 60
flag = True
muerte = False
desaparecer = False
fuerza = 50
puntaje = 0
accion_previa = " "
accion_personaje = "Quieto"
accion_enemigo = "Quieto izquierda"

contador = 0
contador_daño = 0
contador_daño_a_enemigo = 0
contador_daño_a_personaje = 0


ataque_enemigo = 0
ataque_personaje = 0
ataque_enemigo_izq = 0
ataque_personaje_izq = 0

velocidad_kunai = 10
velocidad_flecha = 50

pasar_nivel = 0

lista_monedas = []
primera_moneda = crear_moneda(rectangulo_personaje.x + 100, 820, item_moneda)
lista_monedas.append(primera_moneda)
segunda_moneda = crear_moneda(rectangulo_plataforma.x + 150, 720, item_moneda)
lista_monedas.append(segunda_moneda)
tercera_moneda = crear_moneda(rectangulo_segundo_piso.x + 210, 810, item_moneda)
lista_monedas.append(tercera_moneda)
# Agregar PLATAFORMAS

while flag:
    sleep(0.08)
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            break
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
            update(lista_monedas)
            
    keys = pygame.key.get_pressed()
    
    if (keys[pygame.K_RIGHT]):
        accion_personaje = "Derecha"
        accion_previa = accion_personaje
    elif keys[pygame.K_LEFT] and rectangulo_personaje.x > 0 - velocidad:
        accion_personaje = "Izquierda"
        accion_previa = accion_personaje
    elif keys[pygame.K_UP]:
        accion_personaje = "Salta"
    elif keys[pygame.K_k]:
        if ataque_personaje == 0 or ataque_personaje_izq == 0:
            if accion_previa == "Izquierda":
                accion_personaje = "Ataque izquierda"
                posicion_actual_x = rectangulo_personaje.x
                posicion_actual_y =  rectangulo_personaje.y   
                personaje_flecha.x =  rectangulo_personaje.x
                ataque_personaje_izq = 1
            elif accion_previa == "Derecha":
                accion_personaje = "Ataque"
                posicion_actual_x = rectangulo_personaje.x
                posicion_actual_y =  rectangulo_personaje.y   
                personaje_flecha.x =  rectangulo_personaje.x
                ataque_personaje = 1
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()
    else:
        if accion_personaje == "Izquierda":
            accion_personaje = "Quieto izquierda"
        elif accion_personaje == "Derecha":
            accion_personaje = "Quieto" 
    
    PANTALLA.blit(fondo,(0,0))
    realizar_accion_personaje(PANTALLA, accion_personaje, lados_personaje, velocidad, lista_plataformas)
    
    for moneda in lista_monedas:
        animar_objeto(PANTALLA,moneda["rectangulo"], item_moneda)
        pygame.draw.rect(PANTALLA, "Black", moneda["rectangulo"], 2)
        if rectangulo_personaje.colliderect(moneda["rectangulo"]):
            pygame.mixer.init()
            sonido_recolectar = pygame.mixer.Sound("Moneda.mp3")
            sonido_recolectar.set_volume(0.1)
            sonido_recolectar.play()
            animar_objeto(PANTALLA,moneda["rectangulo"], obtener_item_moneda)
            desaparecer_moneda(moneda["rectangulo"])
            puntaje += 50
        
    if ataque_personaje == 1 and muerte == 0:
        if accion_personaje == "Ataque izquierda":
            mover(personaje_flecha, velocidad_flecha * -1)
            PANTALLA.blit(flecha_atras[0], personaje_flecha)
        elif accion_personaje == "Ataque" :
            mover(personaje_flecha, velocidad_flecha * 1)
            PANTALLA.blit(flecha, personaje_flecha)    
        
    if muerte == False:
        if rectangulo_vision.colliderect(rectangulo_personaje):
            if rectangulo_enemigo.x > rectangulo_personaje.x:
                accion_enemigo = "Ataque izquierda"
                ataque_enemigo_izq = 1
            elif rectangulo_enemigo.x < rectangulo_personaje.x:
                accion_enemigo = "Ataque derecha"
                ataque_enemigo = 1
        else:
            if accion_enemigo == "Ataque derecha":
                accion_enemigo = "Quieto derecha"
            elif accion_enemigo == "Ataque izquierda":
                accion_enemigo = "Quieto izquierda"
        realizar_accion_enemigo(PANTALLA, accion_enemigo, lados_enemigo)
    else:
        if desaparecer == False:
            accion_enemigo = "Muerte"
            realizar_accion_enemigo(PANTALLA, accion_enemigo, lados_enemigo)
            desaparecer = True
    
    if ataque_personaje  == 1:
        mover(personaje_flecha, 50)
        PANTALLA.blit(flecha, personaje_flecha)
    elif ataque_personaje_izq == 1:
        mover(personaje_flecha, -50)
        PANTALLA.blit(flecha_atras[0], personaje_flecha)
        
    if ataque_enemigo == 1:
        animar_objeto(PANTALLA, rectangulo_kunai, personaje_kunai)
        mover(rectangulo_kunai, velocidad_kunai)
    elif ataque_enemigo_izq == 1:
        animar_objeto(PANTALLA, rectangulo_kunai, personaje_kunai)
        mover(rectangulo_kunai, velocidad_kunai * -1)

                
        if rectangulo_kunai.colliderect(rectangulo_personaje):
            ataque_enemigo = 0
            ataque_enemigo_izq = 0
            accion_personaje = "Daño"
            contador_daño_a_personaje += 0.5
            desaparecer_kunai(rectangulo_kunai)
        elif rectangulo_kunai.x > W or rectangulo_kunai.x < 0:
            ataque_enemigo = 0
            ataque_enemigo_izq = 0
            desaparecer_kunai(rectangulo_kunai)
        elif rectangulo_kunai.colliderect(rectangulo_plataforma):
            ataque_enemigo = 0
            ataque_enemigo_izq = 0
            desaparecer_kunai(rectangulo_kunai)
            
    if personaje_flecha.x == (W) or personaje_flecha.x < 0:
        ataque_personaje = 0
        ataque_personaje_izq = 0
        desaparecer_flecha(personaje_flecha, posicion_actual_x,posicion_actual_y)
    elif personaje_flecha.colliderect(rectangulo_plataforma):
        ataque_personaje = 0
        ataque_personaje_izq = 0 
        desaparecer_flecha(personaje_flecha, posicion_actual_x,posicion_actual_y)
    elif personaje_flecha.colliderect(rectangulo_enemigo):
        ataque_personaje = 0
        ataque_personaje_izq = 0
        accion_enemigo = "Muerte"
        contador_daño_a_enemigo += 1
        desaparecer_flecha(personaje_flecha, posicion_actual_x,posicion_actual_y)
        if contador_daño_a_enemigo == 2:
            muerte = True
            puntaje += 100
        
    flag = actualizar_pantalla_daño(PANTALLA,personaje_vida,personaje_menos_una_vida, contador_daño_a_personaje)
    
    logo_tiempo = PANTALLA.blit(pygame.transform.scale(banner_time, (80, 50)), (W / 2 - 30, 10))
    PANTALLA.blit(piso,rectangulo_piso)
    PANTALLA.blit(segundo_piso,rectangulo_segundo_piso)
    
    if rectangulo_personaje.y > H + 400:
        flag = False
    elif  rectangulo_personaje.x  > W + 10:
        puntaje += time
        flag = False
        
    if contador == 15:
        if time > 0:
            time -= 1
            contador = 0
        else:
            time = 0
            pygame.quit()
            flag = False
    
    contador +=1
    tiempo = fuente.render(":{0}".format(time), True, [255, 255, 255])
    score = fuente.render("Score:{0}".format(puntaje), True, [255, 255, 255])
    stronght = fuente.render("Fuerza:{0}".format(fuerza), True, [255, 255, 255])
    PANTALLA.blit(tiempo, (W / 2 + 50, 10))
    PANTALLA.blit(score, (W / 2 + 400, 10))
    PANTALLA.blit(stronght, (W / 2 + 400, 50))
    pygame.display.update()






    # pygame.draw.rect(PANTALLA, "Green", rectangulo_vision, 5)

    # # pygame.draw.rect(PANTALLA, "Red", personaje_flecha, 5)
    # # pygame.draw.rect(PANTALLA, "Red", rectangulo_kunai, 5)

    # # for lado in lados_piso:
    # #     pygame.draw.rect(PANTALLA, "Gold", lados_piso[lado], 2)

    # # for lado in lados_personaje:
    # #     pygame.draw.rect(PANTALLA, "Red", lados_personaje[lado], 2)
    
    # # for lado in lados_enemigo:
    # #     pygame.draw.rect(PANTALLA, "Blue", lados_enemigo[lado], 2)

    # # for lado in lados_plataforma:
    # #     pygame.draw.rect(PANTALLA, "Gold", lados_plataforma[lado], 2)

    # # for lado in lados_segundo_piso:
    # #     pygame.draw.rect(PANTALLA, "Cyan", lados_segundo_piso[lado], 2)
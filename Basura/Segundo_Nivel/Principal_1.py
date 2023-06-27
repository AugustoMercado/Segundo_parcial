import pygame
import random
from Niveles.Personaje import *
from Moneda import *

W, H = 1500, 900
FPS = 18


#############################################################################################
def crear_plataformas (W,H,x,y):
    plataforma = pygame.image.load("Recursos/Plataforma/0.png")
    plataforma = pygame.transform.scale(plataforma, (W, H))  # Jugamos el tamaño con la plataforma
    rectangulo_plataforma = plataforma.get_rect()
    rectangulo_plataforma.x = x
    rectangulo_plataforma.y = y
    
    return rectangulo_plataforma



def obtener_rectangulos(principal: pygame.Rect):
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(
        principal.left, principal.bottom - 10, principal.width, 10
    )
    diccionario["right"] = pygame.Rect(
        principal.right - 2, principal.top, 2, principal.height
    )
    diccionario["left"] = pygame.Rect(
        principal.left, principal.top, 2, principal.height
    )
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 6)

    return diccionario

def aplicar_gravedad(pantalla, personaje_animacion, rectangulo_personaje: pygame.Rect, piso: pygame.Rect):
    global desplazamiento_y, esta_saltando

    if esta_saltando:
        animar(pantalla, rectangulo_personaje, personaje_animacion)

    rectangulo_personaje.y += desplazamiento_y
    if desplazamiento_y + gravedad < limite_velocidad_caida:
        desplazamiento_y += gravedad
    if rectangulo_personaje.colliderect(piso):
        esta_saltando = False
        desplazamiento_y = 0
        rectangulo_personaje.bottom = piso.top


def aplicar_gravedad(
    pantalla, personaje_animacion, rectangulo_personaje: pygame.Rect, lados_pisos: list
):
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


def realizar_accion_personaje(
    pantalla, accion_personaje, lados_personaje, velocidad, plataformas):
    global desplazamiento_y, esta_saltando


    pantalla.blit(fondo, (0, 0))
    pantalla.blit(plataforma, (plataforma.x, plataforma.y))

    match accion_personaje:
        case "Derecha":
            if not esta_saltando:
                animar(pantalla, lados_personaje["main"], personaje_camina)
                mover_personaje(lados_personaje, velocidad)
        case "Izquierda":
            if not esta_saltando:
                animar(pantalla, lados_personaje["main"], personaje_camina_izquierda)
                mover_personaje(lados_personaje, velocidad * -1)
        case "Ataque":
            if not esta_saltando:
                animar(pantalla, lados_personaje["main"], personaje_ataque)
        case "Ataque izquierda":
            if not esta_saltando:
                animar(pantalla, lados_personaje["main"], personaje_ataque)
        case "Salta":
            if not esta_saltando:
                esta_saltando = True
                desplazamiento_y = potencia_salto
                animar(pantalla, lados_personaje["main"], personaje_salta)
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



pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))
# FONDO
fondo = pygame.image.load("Recursos/Fondo/2do Nivel.jpg")
fondo = pygame.transform.scale(fondo, (W, H))
###########################
# Tiempo
time = 5
banner_time = pygame.image.load("Recursos/Tiempo/1.png")

# Fuente
fuente = pygame.font.SysFont("ALGERIAN", 40)
# Score
puntaje = 0

#Musica
# pygame.mixer.init()
# sonido_recolectar = pygame.mixer.Sound("LAST CHANCE.mp3")
# sonido_recolectar.set_volume(0.5)
# sonido_recolectar.play()

########################################################################################################
# PERSONAJE
rectangulo_personaje = personaje_quieto[0].get_rect()
rectangulo_personaje.x = W / 2 - 700
rectangulo_personaje.y = 450

lados_personaje = obtener_rectangulos(rectangulo_personaje)

personaje_vida = pygame.image.load("Recursos/VIDA/0.png")


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


##############################################################################
item_especial = pygame.image.load("Recursos/item_especial/0.png")

lista_animaciones_objetos = [item_moneda, obtener_item_moneda]


#################################################################################

reescalar_imagenes(lista_animaciones, 80, 75)
reescalar_imagenes(lista_animaciones_objetos, 20, 40)

##########################################################################
#salto
gravedad = 1
potencia_salto = -15
limite_velocidad_caida = 20
esta_saltando = False
desplazamiento_y = 0

########################################################################################################
# SUPERFICIE
# piso_uno = pygame.Rect(0, 0, 130, 470)
piso_uno = pygame.image.load("Recursos/Plataforma/0.png")
piso_uno = pygame.transform.scale(piso_uno, (150, 470)) 
rectangulo_piso = piso_uno.get_rect()
rectangulo_piso.top = rectangulo_personaje.bottom
rectangulo_piso.x = 420
rectangulo_piso.y = 780

lados_piso = obtener_rectangulos(rectangulo_piso)

# piso_dos = pygame.Rect(W/2 - 400, 0, W, 20)



########################################################################################################

# trampa_plataforma = [
#     pygame.image.load("Recursos/Trampa/0.png"),
#     pygame.image.load("Recursos/Trampa/1.png"),
#     pygame.image.load("Recursos/Trampa/2.png"),
#     pygame.image.load("Recursos/Trampa/4.png"),
#     pygame.image.load("Recursos/Trampa/5.png"),
#     pygame.image.load("Recursos/Trampa/6.png"),
#     pygame.image.load("Recursos/Trampa/7.png"),
#     pygame.image.load("Recursos/Trampa/8.png"),
#     pygame.image.load("Recursos/Trampa/9.png"),
#     pygame.image.load("Recursos/Trampa/10.png"),
#     pygame.image.load("Recursos/Trampa/11.png"),
#     pygame.image.load("Recursos/Trampa/12.png")
# ]

# rectangulo_trampa = trampa_plataforma[0].get_rect()
# rectangulo_trampa.x = 500
# rectangulo_trampa.y =  600
# lista_plataforma_trampa = [trampa_plataforma]
# reescalar_imagenes(lista_plataforma_trampa, 20, 40)
# lados_plataforma_trampa = obtener_rectangulos(rectangulo_trampa)

######################################################################

plataforma = crear_plataformas(350,20,420,780)





lados_plataforma = obtener_rectangulos(plataforma)

######################################################################

segunda_plataforma = crear_plataformas(350,20,420,780)

lados_segunda_plataforma = obtener_rectangulos(segunda_plataforma)


lista_plataformas = [lados_piso, lados_plataforma, lados_segunda_plataforma]


ataque = 0
flag = True
time = 60
accion_enemigo = "Quieto"
puntaje = 0

lista_monedas = crear_lista_monedas(W,3,item_moneda)

while flag:
    
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            break
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
        if evento.type == pygame.USEREVENT:
            update(lista_monedas)
            

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
        ataque = 1
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()
    else:
        accion_personaje = "Quieto"

    PANTALLA.blit(fondo, (0, 0))

    vida_1 = PANTALLA.blit(pygame.transform.scale(personaje_vida, (80, 80)), (80, 10))
    
    realizar_accion_personaje(PANTALLA,accion_personaje, lados_personaje, velocidad, lista_plataformas)
    
    if ataque == 1 and personaje_flecha < W:
        mover_personaje (personaje_flecha, 10)
        if personaje_flecha.x == (W):
            personaje_flecha.x = rectangulo_personaje.x
            ataque = 0
            
    animar(PANTALLA,lados_plataforma_trampa,lista_plataforma_trampa)
    
    # for moneda in lista_monedas:
    #     # animar(PANTALLA,moneda["rectangulo"], item_moneda)
    #     # if rectangulo_personaje.colliderect(moneda["rectangulo"]):
    #     #     pygame.mixer.init()
    #     #     sonido_recolectar = pygame.mixer.Sound("Moneda.mp3")
    #     #     sonido_recolectar.set_volume(1)
    #     #     sonido_recolectar.play()
    #     #     animar(PANTALLA,moneda["rectangulo"], obtener_item_moneda)
    #     #     desaparecer_moneda(moneda["rectangulo"])
    #     #     puntaje += 100


    logo_tiempo = PANTALLA.blit(pygame.transform.scale(banner_time, (80, 50)), (W / 2 - 30, 10))
    # pygame.draw.rect(PANTALLA, "Gold", piso_uno, 10)
    
    # for lado in lados_piso:
    #     pygame.draw.rect(PANTALLA, "Gold", lados_piso[lado], 10)

    
    # for lado in lados_segunda_plataforma:
    #         pygame.draw.rect(PANTALLA, "Cyan", lados_segunda_plataforma[lado], 10)

    # for lado in lados_plataforma:
    #     pygame.draw.rect(PANTALLA, "Green", lados_plataforma[lado], 2)

    
    # if time > 0:
    #     time -= 1
    # else:
    #     time = 0
    #     pygame.quit()
    #     flag = False

    tiempo = fuente.render(":{0}".format(time), True, [255, 255, 255])
    score = fuente.render("Score:{0}".format(puntaje),True,[255, 255, 255])
    # print (puntaje)
    PANTALLA.blit(tiempo, (W / 2 + 50, 10))
    PANTALLA.blit(score, (W /2 + 400,10))

    
    pygame.display.update()

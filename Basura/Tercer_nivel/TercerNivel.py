import pygame

from Boss import *
from Moneda import *
from time import sleep
from Personaje import *

FPS = 30


#############################################################################################
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


def mover_objeto(rectangulo_personaje: pygame.Rect, velocidad):
    rectangulo_personaje.x += velocidad


def animar(pantalla, rectangulo_personaje, accion_personaje):
    global contador_pasos
    largo = len(accion_personaje)
    if contador_pasos >= largo:
        contador_pasos = 0

    pantalla.blit(accion_personaje[contador_pasos], rectangulo_personaje)
    contador_pasos += 1
    
def animar_boss(pantalla, rectangulo_personaje, accion_personaje):
    global contador_pasos_boss
    largo = len(accion_personaje)
    if contador_pasos_boss >= largo:
        contador_pasos_boss = 0

    pantalla.blit(accion_personaje[contador_pasos_boss], rectangulo_personaje)
    contador_pasos_boss += 1



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
    
def realizar_accion_boss(pantalla, accion_enemigo, lados_enemigo):
    
    match accion_enemigo:
        case "Quieto":
                animar_boss(pantalla, lados_enemigo["main"], boss_quieto)
        case "Quieto izquierda":
                animar_boss(pantalla, lados_enemigo["main"], boss_quieto_izquierda)
        case "Ataque uno":
                animar_boss(pantalla, lados_enemigo["main"], boss_ataque_uno)
        case "Ataque uno izquierda":
                animar_boss(pantalla, lados_enemigo["main"], boss_ataque_uno_izquierda)
        case "Ataque dos":
                animar_boss(pantalla, lados_enemigo["main"], boss_ataque_dos)
        case "Ataque dos izquierda":
                animar_boss(pantalla, lados_enemigo["main"], boss_ataque_dos_izquierda)
        case "Daño":
                animar_boss(pantalla, lados_enemigo["main"], boss_daño)

    

def desaparecer_flecha(personaje_flecha, posicion_actual_x,  posicion_actual_y):
    personaje_flecha.x = posicion_actual_x
    personaje_flecha.y = posicion_actual_y + 30
    
    
########################################################################################################
pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))
# FONDO
fondo = pygame.image.load("Recursos/Fondo/3er Nivel.jpg")
fondo = pygame.transform.scale(fondo, (W, H))
###########################
# Tiempo
time = 60
TIEMPO = pygame.time.Clock()
banner_time = pygame.image.load("Recursos/Tiempo/1.png")

# Fuente
fuente = pygame.font.SysFont("ALGERIAN", 40)
# Score
puntaje = 0

# Musica
pygame.mixer.init()
sonido_recolectar = pygame.mixer.Sound("BORN TO OWN.mp3")
sonido_recolectar.set_volume(0.2)
sonido_recolectar.play()
########################################################################################################
# PERSONAJE
rectangulo_personaje = personaje_quieto[0].get_rect()
rectangulo_personaje.x = W / 2 - 700
rectangulo_personaje.y = 750

lados_personaje = obtener_rectangulos(rectangulo_personaje)

personaje_vida = pygame.image.load("Recursos/VIDA/0.png")
personaje_menos_una_vida = pygame.image.load("Recursos/VIDA/cruz rojaa.png")

contador_pasos = 0

velocidad = 5

# salto
gravedad = 1
potencia_salto = -15
limite_velocidad_caida = 20
esta_saltando = False
desplazamiento_y = 0
desplazamiento_x = 0
posicion_actual_x = 0
posicion_actual_y = 0



lista_quieto = [personaje_quieto, personaje_quieto_izquierda]

lista_animaciones = [
    personaje_camina,
    personaje_camina_izquierda,
    personaje_daño,
    personaje_ataque,
    personaje_ataque_izquierda,
]


flecha = pygame.image.load("Recursos/Personaje/Ataque/Flecha/0.png")
personaje_flecha = (pygame.transform.scale(flecha, (55, 25))).get_rect()
personaje_flecha.x = rectangulo_personaje.x
personaje_flecha.y = rectangulo_personaje.y - 20
########################################################################################################
#BOSS

rectangulo_boss = boss_quieto[0].get_rect()
rectangulo_boss.x = W - 600
rectangulo_boss.y = 780
rectangulo_boss.width = 100

rectangulo_espada = boss_ataque_uno[0].get_rect()
rectangulo_espada.x = rectangulo_boss.x 
rectangulo_espada.y = rectangulo_boss.y 
rectangulo_espada.width = 80
rectangulo_espada.height = 80


# hacer un rectangulo de vision y adentro un rectangulo del personaje.
lados_boss = obtener_rectangulos(rectangulo_boss)



lista_animaciones_boss = [
    boss_quieto,
    boss_quieto_izquierda,
    boss_ataque_uno,
    boss_ataque_uno_izquierda,
    boss_ataque_dos,
    boss_ataque_dos_izquierda,
    boss_daño,
]


##############################################################################
item_especial = pygame.image.load("Recursos/item_especial/0.png")
pocima = (pygame.transform.scale(item_especial,(40, 40))).get_rect()
pocima.x = 820
pocima.y = 650

item_vida = pygame.image.load("Recursos/item_especial/1.png")
pocima_vida = (pygame.transform.scale(item_especial,(40, 40))).get_rect()
pocima_vida.x = random.randrange(0, W, 50)
pocima_vida.y = random.randrange(700, 800, 50)


lados_item_especial = obtener_rectangulos(pocima)
lados_item_vida = obtener_rectangulos(pocima_vida)

lista_animaciones_objetos = [item_moneda, obtener_item_moneda]

#################################################################################
reescalar_imagenes(lista_quieto, 47, 102)
# reescalar_imagenes(lista_animaciones, 80, 75)
reescalar_imagenes(lista_animaciones_boss, 100, 100)
reescalar_imagenes(lista_animaciones_objetos, 20, 40)

########################################################################################################

piso_uno = pygame.image.load("Recursos/Plataforma/0.png")
piso_uno = pygame.transform.scale(piso_uno, (W, 470))
rectangulo_piso = piso_uno.get_rect()
rectangulo_piso.x = 0
rectangulo_piso.top = 870


lados_piso = obtener_rectangulos(rectangulo_piso)
########################################################################################################

plataforma = pygame.image.load("Recursos/Plataforma/0.png")
plataforma = pygame.transform.scale(plataforma, (350, 20))
rectangulo_plataforma = plataforma.get_rect()
rectangulo_plataforma.x = W / 2 - 500
rectangulo_plataforma.y = 740

lados_plataforma = obtener_rectangulos(rectangulo_plataforma)


segunda_plataforma = pygame.image.load("Recursos/Plataforma/0.png")
segunda_plataforma = pygame.transform.scale(plataforma, (350, 20))
rectangulo_segunda_plataforma = segunda_plataforma.get_rect()
rectangulo_segunda_plataforma.x = W / 2 
rectangulo_segunda_plataforma.y = 740

lados_segunda_plataforma = obtener_rectangulos(rectangulo_segunda_plataforma)

########################################################################################################

lista_plataformas = [lados_piso,lados_plataforma,lados_segunda_plataforma ]
lista_monedas = crear_lista_monedas(W,3, item_moneda)


accion_previa = " "
accion_boss = "Quieto"
accion_personaje = "Quieto"

time = 51
ataque = 0
fuerza = 150
flag = True
puntaje = 0
contador = 0
muerte = False
contador_daño = 0
contador_daño_a_personaje = 0
contador_daño_a_boss = 0
teletransporte = 0
ataque_personaje = 0



while flag:
    sleep(0.08)
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            break
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)


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
    
    realizar_accion_personaje(PANTALLA, accion_personaje, lados_personaje, velocidad, lista_plataformas)
    
    if muerte_boos != True:
        if rectangulo_boss.x > rectangulo_personaje.x:
            if rectangulo_boss.colliderect(rectangulo_personaje):
                accion_boss = "Ataque uno izquierda"
                ataque_enemigo = 1
            else:
                accion_boss = "Quieto izquierda"
        elif rectangulo_boss.x < rectangulo_personaje.x:
            if rectangulo_boss.colliderect(rectangulo_personaje):
                accion_boss = "Ataque uno"
                ataque_enemigo = 1
            else:
                accion_boss = "Quieto"
        realizar_accion_boss(PANTALLA, accion_boss, lados_boss)
    else:
        accion_boss = "Daño"
        realizar_accion_boss(PANTALLA, accion_boss, lados_boss)
            
    if rectangulo_espada.colliderect(rectangulo_personaje):
        contador_daño += 1
        if contador_daño == 10:
            contador_daño_a_personaje += 1
            contador_daño = 0
                
    if ataque_personaje  == 1:
        mover_objeto(personaje_flecha, 50)
        PANTALLA.blit(flecha, personaje_flecha)
    elif ataque_personaje_izq == 1:
        mover_objeto(personaje_flecha, -50)
        # PANTALLA.blit(flecha_atras[0], personaje_flecha)
    
    if personaje_flecha.x > W + 100 or personaje_flecha.x < 0:
        ataque_personaje = 0
        ataque_personaje_izq = 0
        desaparecer_flecha(personaje_flecha, posicion_actual_x,  posicion_actual_y)
    elif personaje_flecha.colliderect(rectangulo_boss) and (ataque_personaje == 1 or ataque_personaje_izq == 1):
        ataque_personaje = 0
        ataque_personaje_izq = 0
        accion_enemigo = "Daño"
        contador_daño_a_boss += 0.5
        if fuerza_antigua  > fuerza:
            contador_daño_a_boss += 1
        desaparecer_flecha(personaje_flecha, posicion_actual_x,  posicion_actual_y)
    

    PANTALLA.blit(item_especial,pocima)
    if rectangulo_personaje.colliderect(lados_item_especial["main"]):
        desaparecer_moneda(lados_item_especial["main"])
        fuerza += 100
        fuerza_antigua = fuerza
        
    # if contador_daño_a_personaje > 0:   
    #     PANTALLA.blit(item_vida,primera_pocima["rectangulo"])
    #     PANTALLA.blit(item_vida,segunda_pocima["rectangulo"])
    #     PANTALLA.blit(item_vida,tercera_pocima["rectangulo"])
        
    #     if rectangulo_personaje.colliderect(primera_pocima["rectangulo"]):
    #         desaparecer_moneda(primera_pocima["rectangulo"])
    #         contador_daño_a_personaje -= 1
    #     elif rectangulo_personaje.colliderect(segunda_pocima["rectangulo"]):
    #         desaparecer_moneda(segunda_pocima["rectangulo"])
    #         contador_daño_a_personaje -= 1
    #     elif rectangulo_personaje.colliderect(tercera_pocima["rectangulo"]):
    #         desaparecer_moneda(tercera_pocima["rectangulo"])
    #         contador_daño_a_personaje -= 1

    if muerte_boos == True:
        puntaje += 1000
        stop_time = True
        
    if muerte_boos != True:
        if contador == 10:
            teletransporte += 1
            if teletransporte == 10:
                rectangulo_boss.x = rectangulo_personaje.x - 10
                rectangulo_espada.x = rectangulo_boss.x
                teletransporte = 0

    flag = actualizar_pantalla_daño (PANTALLA, personaje_vida,personaje_menos_una_vida, contador_daño_a_personaje)
    
    muerte_boos = actualizar_pantalla_daño_boss (PANTALLA, personaje_vida,personaje_menos_una_vida, contador_daño_a_boss)
                
    PANTALLA.blit(piso_uno,lados_piso["main"])
    PANTALLA.blit(plataforma,rectangulo_plataforma)
    PANTALLA.blit(segunda_plataforma,rectangulo_segunda_plataforma)

    if contador == 15 :
        if time > 0:
            if stop_time != True:
                time -= 1
                contador = 0
        else:
            time = 0
            pygame.quit()
            flag = False
    
    contador += 1
    
    tiempo = fuente.render(":{0}".format(time), True, [255, 255, 255])
    puntaje_jugador = fuente.render("Score:{0}".format(puntaje), True, [255, 255, 255])
    fuerza_personaje = fuente.render("Fuerza:{0}".format(fuerza), True, [255, 255, 255])
    PANTALLA.blit(tiempo, (W / 2 + 50, 10))
    PANTALLA.blit(puntaje_jugador, (W / 2 + 400, 10))
    PANTALLA.blit(fuerza_personaje, (W / 2 + 400, 50))
    
    pygame.display.update()
    
    # for lado in lados_piso:
    #     pygame.draw.rect(PANTALLA, "Gold", lados_piso[lado], 2)

    # for lado in lados_plataforma:
    #     pygame.draw.rect(PANTALLA, "Green", lados_plataforma[lado], 2)

    # for lado in lados_item_vida:
    #     pygame.draw.rect(PANTALLA, "Green", lados_item_vida[lado], 2)

    # for lado in lados_item_especial:
    #     pygame.draw.rect(PANTALLA, "Blue", lados_item_especial[lado], 2)

    # for lado in lados_personaje:
    #     pygame.draw.rect(PANTALLA, "Red", lados_personaje[lado], 2)

    # for lado in lados_boss:
    #     pygame.draw.rect(PANTALLA, "Blue", lados_boss[lado], 2)

    # pygame.draw.rect(PANTALLA, "Green", pocima_vida, 2)
    # pygame.draw.rect(PANTALLA, "Green", pocima_vida, 2)
    # pygame.draw.rect(PANTALLA, "Green", pocima_vida, 2)

    # pygame.draw.rect(PANTALLA, "Red", personaje_flecha, 2)
    
        # pygame.draw.rect(PANTALLA, "Red", personaje_flecha, 2)
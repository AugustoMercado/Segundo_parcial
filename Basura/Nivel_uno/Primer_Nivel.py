import pygame
from time import sleep
import random
from Niveles.Personaje import *
from Niveles.Configuraciones import *
from Niveles.Class_Personaje import Personaje
from Niveles.Class_Plataforma import Plataforma
from Niveles.Modo import *

W, H = 1500, 900
FPS = 18
def actualizar_pantalla (pantalla,mi_personaje: Personaje,fondo,plataformas):
    pantalla.blit(fondo,(0,0))
    mi_personaje.update(pantalla,plataformas)

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
# rectangulo_personaje = personaje_quieto[0].get_rect()
tamaño = (70,85)
posicion_incial = (W / 2 - 500,790)
velocidad = 5
animaciones = {}
animaciones["Quieto"] = personaje_quieto
animaciones["Quieto izquierda"] = personaje_quieto_izquierda
animaciones["Derecha"] = personaje_camina
animaciones["Izquierda"] = personaje_camina_izquierda
animaciones["Ataque"] = personaje_ataque
animaciones["Ataque izquierda"] = personaje_ataque_izquierda
animaciones["Salta"] = personaje_salta
animaciones["Daño"] = personaje_daño

mi_personaje = Personaje(tamaño,animaciones,posicion_incial,velocidad)

personaje_vida = pygame.image.load("Recursos/VIDA/0.png")

flecha = pygame.image.load("Recursos/Personaje/Ataque/Flecha/0.png")
personaje_flecha = (pygame.transform.scale(flecha, (55, 25))).get_rect()
personaje_flecha.x = mi_personaje.lados["main"].left
personaje_flecha.y = 830
#######################################################################################################

########################################################################################################
# # SUPERFICIE
piso = pygame.image.load("Recursos/Plataforma/0.png")
piso = pygame.transform.scale(piso, (W / 2, 30))
piso_rect = piso.get_rect()
piso_rect.top = mi_personaje.lados["main"].bottom

lados_piso = obtener_rectangulos(piso_rect)

Platform = Plataforma("Recursos/Plataforma/0.png",(350,30),(420,780))
# plataforma = pygame.image.load("Recursos/Plataforma/0.png")
# plataforma = pygame.transform.scale(plataforma, (350, 20))  # Jugamos el tamaño con la plataforma
# rectangulo_plataforma = plataforma.get_rect()
# rectangulo_plataforma.x = 420
# rectangulo_plataforma.y = 780

# lados_plataforma = obtener_rectangulos(rectangulo_plataforma)

lista_plataformas = [lados_piso, Platform.lados_plataforma]

#########################################################


ataque = 0
flag = True
time = 60
puntaje = 0
delay = 15

accion_previa = " "
# lista_monedas = crear_lista_monedas(W,3,item_moneda)

while flag:
    
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            break
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_TAB:
            cambiar_modo()
            
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_RIGHT]):
        mi_personaje.accion = "Derecha"
        accion_previa = mi_personaje.accion
    elif keys[pygame.K_LEFT]:
        mi_personaje.accion = "Izquierda"
        accion_previa = mi_personaje.accion
    elif keys[pygame.K_UP]:
        mi_personaje.accion = "Salta"
    elif keys[pygame.K_k]:
        mi_personaje.accion = "Ataque"
        ataque_personaje = 1
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()
    else:
        if mi_personaje.accion == "izquierda":
            mi_personaje.accion = "Quieto izquierda"
        elif mi_personaje.accion == "Derecha":
            mi_personaje.accion = "Quieto"
            
            
    PANTALLA.blit(fondo, (0, 0))
    vida_1 = PANTALLA.blit(pygame.transform.scale(personaje_vida, (80, 80)), (80, 10))
    
    actualizar_pantalla(PANTALLA,mi_personaje,fondo,lista_plataformas)
    
    logo_tiempo = PANTALLA.blit(pygame.transform.scale(banner_time, (80, 50)), (W / 2 - 30, 10))

    

    PANTALLA.blit(piso,piso_rect)
    PANTALLA.blit(Platform.base_plataforma,Platform.lados_plataforma["main"])
    
    
    if get_modo():
        
        for lado in lados_piso:
            pygame.draw.rect(PANTALLA, "Blue", lados_piso[lado],3)
            
        for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA, "Red", mi_personaje.lados[lado],3)
        
        for lado in Platform.lados_plataforma:
            pygame.draw.rect(PANTALLA, "Red", Platform.lados_plataforma[lado],3)
    
    # if time > 0:
    #     time -= 1
    # else:
    #     time = 0
    #     pygame.quit()
    #     flag = False

    tiempo = fuente.render(":{0}".format(time), True, [255, 255, 255])
    score = fuente.render("Score:{0}".format(puntaje),True,[255, 255, 255])
    PANTALLA.blit(tiempo, (W / 2 + 50, 10))
    PANTALLA.blit(score, (W /2 + 300,10))
    pygame.display.update()

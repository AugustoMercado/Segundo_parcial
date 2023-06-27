import pygame
import random
from Niveles.Personaje import *

    
def actualizar_pantalla_daño_boss (pantalla, personaje_vida,personaje_menos_una_vida, contador_daño_a_boss):
    muerte_boos = False
    if contador_daño_a_boss <= 1:
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1000, 100))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1100, 100))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1200, 100))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1300, 100))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1400, 100))
    elif contador_daño_a_boss > 1 and contador_daño_a_boss <=3:
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1000, 100))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1100, 100))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1200, 100))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1300, 100))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1400, 100))
    elif contador_daño_a_boss > 3 and contador_daño_a_boss <= 6:
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1000, 100))
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1100, 100))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1200, 100))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1300, 100))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1400, 100))
    elif  contador_daño_a_boss > 6 and contador_daño_a_boss <= 9:
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1000, 100))
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1100, 100))
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1200, 100))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1300, 100))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1400, 100))
    elif  contador_daño_a_boss > 9 and contador_daño_a_boss <= 11:
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1000, 100))
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1100, 100))
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1200, 100))
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1300, 100))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (1400, 100))
    elif contador_daño_a_boss == 12:
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1000, 100))
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1100, 100))
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1200, 100))
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1300, 100))
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1400, 100))
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (280, 20))
        muerte_boos = True
    return muerte_boos

boss_quieto = [
    pygame.image.load("Recursos/Boss/1.png"),
    pygame.image.load("Recursos/Boss/2.png"),
    pygame.image.load("Recursos/Boss/3.png"),
]


boss_ataque_uno = [
    pygame.image.load("Recursos/Boss/7.png"),
    pygame.image.load("Recursos/Boss/7.png"),
    pygame.image.load("Recursos/Boss/7.png"),
    pygame.image.load("Recursos/Boss/7.png"),
    pygame.image.load("Recursos/Boss/7.png"),
    pygame.image.load("Recursos/Boss/7.png"),
    pygame.image.load("Recursos/Boss/9.png"),
    pygame.image.load("Recursos/Boss/8.png"),
]

boss_ataque_dos = [
    pygame.image.load("Recursos/Boss/7.png"),
    pygame.image.load("Recursos/Boss/7.png"),
    pygame.image.load("Recursos/Boss/7.png"),
    pygame.image.load("Recursos/Boss/7.png"),
    pygame.image.load("Recursos/Boss/7.png"),
    pygame.image.load("Recursos/Boss/7.png"),
    pygame.image.load("Recursos/Boss/4.png"),
    pygame.image.load("Recursos/Boss/4.png"),
]



boss_daño = [
    pygame.image.load("Recursos/Boss/5.png"),
    pygame.image.load("Recursos/Boss/6.png")
]


boss_quieto_izquierda = girar_imagen(boss_quieto,True,False)
boss_ataque_uno_izquierda = girar_imagen(boss_ataque_uno,True,False)
boss_ataque_dos_izquierda = girar_imagen(boss_ataque_dos,True,False)
boss_daño_izquierda = girar_imagen(boss_daño, True, False)
import pygame
import random
from Niveles.Personaje import *



vida_boos = pygame.image.load("Recursos/imagenes/vida_samurai.png")


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



boss_daño = [
    pygame.image.load("Recursos/Boss/5.png"),
    pygame.image.load("Recursos/Boss/6.png")
]


boss_quieto_izquierda = girar_imagen(boss_quieto,True,False)
boss_ataque_uno_izquierda = girar_imagen(boss_ataque_uno,True,False)


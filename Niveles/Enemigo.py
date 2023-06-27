import pygame
import random
from Niveles.Personaje import *


def crear_cantidad_enemigos(cantidad):
    lista_enemigos = []
    for i in range(cantidad):
        rectangulo_enemigo = personaje_enemigo_quieto[0].get_rect()
        rectangulo_enemigo.x = random.randrange(500,750,50)
        rectangulo_enemigo.y = 800
        rectangulo_enemigo.width = 500
        rectangulo_enemigo.height = 80
    return lista_enemigos
    
def actualizar_pantalla_kunai(lista_enemigos,personaje):
    for kunai in lista_enemigos:
        if personaje.colliderect(kunai["rectangulo"]):
            #agg sonidos de dolor
            personaje["puntaje"] -= 100
            desaparecer_kunai(kunai)
        elif kunai["rectangulo"].x > 800:
            desaparecer_kunai(kunai)  
            


def desaparecer_kunai(enemigo):
    enemigo["rectangulo"].x = random.randrange(0,748,60)
    

personaje_enemigo_quieto = [
    pygame.image.load("Recursos/Enemigo/quieto/0.png"),
    pygame.image.load("Recursos/Enemigo/quieto/1.png"),
    pygame.image.load("Recursos/Enemigo/quieto/2.png"),
    pygame.image.load("Recursos/Enemigo/quieto/3.png"),
    pygame.image.load("Recursos/Enemigo/quieto/4.png"),
    pygame.image.load("Recursos/Enemigo/quieto/5.png"),
    pygame.image.load("Recursos/Enemigo/quieto/6.png"),
]


personaje_enemigo_ataca = [
    pygame.image.load("Recursos/Enemigo/Ataque/0.png"),
    pygame.image.load("Recursos/Enemigo/Ataque/1.png"),
    pygame.image.load("Recursos/Enemigo/Ataque/2.png"),
    pygame.image.load("Recursos/Enemigo/Ataque/3.png"),
    pygame.image.load("Recursos/Enemigo/Ataque/4.png"),
    pygame.image.load("Recursos/Enemigo/Ataque/5.png"),
    pygame.image.load("Recursos/Enemigo/Ataque/6.png"),
]

personaje_kunai = [
    pygame.image.load("Recursos/Enemigo/Ataque/kunaii/0.png"),
    pygame.image.load("Recursos/Enemigo/Ataque/kunaii/1.png"),
    pygame.image.load("Recursos/Enemigo/Ataque/kunaii/2.png"),
    pygame.image.load("Recursos/Enemigo/Ataque/kunaii/0.png"),
    pygame.image.load("Recursos/Enemigo/Ataque/kunaii/1.png"),
    pygame.image.load("Recursos/Enemigo/Ataque/kunaii/2.png")
]

personaje_muerte = [
    pygame.image.load("Recursos/Enemigo/Muerte/0.png"),
    pygame.image.load("Recursos/Enemigo/Muerte/1.png"),
    pygame.image.load("Recursos/Enemigo/Muerte/2.png"),
    pygame.image.load("Recursos/Enemigo/Muerte/3.png"),
    pygame.image.load("Recursos/Enemigo/Muerte/4.png"),
]


trampa_quieta = [pygame.image.load("Recursos/Trampa/hola/0.png")]

trampa_ataque = [
    pygame.image.load("Recursos/Trampa/hola/1.png"),
    pygame.image.load("Recursos/Trampa/hola/2.png"),
    pygame.image.load("Recursos/Trampa/hola/4.png"),
    pygame.image.load("Recursos/Trampa/hola/5.png"),
    pygame.image.load("Recursos/Trampa/hola/6.png")
]


personaje_enemigo_quieto_izquierda = girar_imagen(personaje_enemigo_quieto, True, False)
personaje_enemigo_ataca_izquierda = girar_imagen(personaje_enemigo_ataca, True, False)
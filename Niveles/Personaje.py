import pygame
from Niveles.Configuraciones import girar_imagen

personaje_vida = pygame.image.load("Recursos/VIDA/0.png")

personaje_menos_una_vida = pygame.image.load("Recursos/VIDA/cruz rojaa.png")

item_especial = pygame.image.load("Recursos/item_especial/0.png")
pocima = (pygame.transform.scale(item_especial,(40, 40))).get_rect()

        
personaje_quieto = [
    pygame.image.load("Recursos/Personaje/Quieto/0.png"),
    pygame.image.load("Recursos/Personaje/Quieto/1.png"),
    pygame.image.load("Recursos/Personaje/Quieto/2.png"),
    pygame.image.load("Recursos/Personaje/Quieto/3.png"),
    pygame.image.load("Recursos/Personaje/Quieto/4.png") 
]

personaje_camina = [
    pygame.image.load("Recursos/Personaje/Camina/0.png"),
    pygame.image.load("Recursos/Personaje/Camina/1.png"),
    pygame.image.load("Recursos/Personaje/Camina/2.png"),
    pygame.image.load("Recursos/Personaje/Camina/3.png"),
    pygame.image.load("Recursos/Personaje/Camina/4.png"),
    pygame.image.load("Recursos/Personaje/Camina/5.png"),  
    pygame.image.load("Recursos/Personaje/Camina/6.png"),
    pygame.image.load("Recursos/Personaje/Camina/7.png"),
]

personaje_salta = [
    pygame.image.load("Recursos/Personaje/Saltar/0.png"),
    pygame.image.load("Recursos/Personaje/Saltar/1.png"),
    pygame.image.load("Recursos/Personaje/Saltar/2.png"),
    pygame.image.load("Recursos/Personaje/Saltar/3.png"),
    pygame.image.load("Recursos/Personaje/Saltar/4.png"),
    pygame.image.load("Recursos/Personaje/Saltar/5.png"),
    pygame.image.load("Recursos/Personaje/Saltar/6.png"),
    pygame.image.load("Recursos/Personaje/Saltar/7.png"),
]

personaje_corre = [
    pygame.image.load("Recursos/Personaje/Corre/0.png"),
    pygame.image.load("Recursos/Personaje/Corre/1.png"),
    pygame.image.load("Recursos/Personaje/Corre/2.png"),
    pygame.image.load("Recursos/Personaje/Corre/3.png"),
    pygame.image.load("Recursos/Personaje/Corre/4.png"),
    pygame.image.load("Recursos/Personaje/Corre/5.png"),
    pygame.image.load("Recursos/Personaje/Corre/6.png"),
    pygame.image.load("Recursos/Personaje/Corre/7.png"),
]

personaje_daño = [
    pygame.image.load("Recursos/Personaje/Muerte/0.png"),
    pygame.image.load("Recursos/Personaje/Muerte/1.png"),
    pygame.image.load("Recursos/Personaje/Muerte/0.png"),
    pygame.image.load("Recursos/Personaje/Muerte/1.png"),
    pygame.image.load("Recursos/Personaje/Muerte/0.png"),
    pygame.image.load("Recursos/Personaje/Muerte/1.png")
]

personaje_ataque = [
    pygame.image.load("Recursos/Personaje/Ataque/0.png"),
    pygame.image.load("Recursos/Personaje/Ataque/1.png"),
    pygame.image.load("Recursos/Personaje/Ataque/2.png"),
    pygame.image.load("Recursos/Personaje/Ataque/3.png"),
    pygame.image.load("Recursos/Personaje/Ataque/4.png"),
    pygame.image.load("Recursos/Personaje/Ataque/5.png"),
    pygame.image.load("Recursos/Personaje/Ataque/6.png"),
    pygame.image.load("Recursos/Personaje/Ataque/7.png"),
    pygame.image.load("Recursos/Personaje/Ataque/8.png"),
    pygame.image.load("Recursos/Personaje/Ataque/9.png"),
    pygame.image.load("Recursos/Personaje/Ataque/10.png"),
    pygame.image.load("Recursos/Personaje/Ataque/11.png"),
    pygame.image.load("Recursos/Personaje/Ataque/12.png")
]
Flecha = [
    pygame.image.load("Recursos/Personaje/Ataque/Flecha/0.png"), 
]


personaje_quieto_izquierda = girar_imagen(personaje_quieto,True,False)
personaje_camina_izquierda = girar_imagen(personaje_camina,True,False)
personaje_ataque_izquierda = girar_imagen(personaje_ataque, True, False)
Flecha_atras = girar_imagen(Flecha, True, False)
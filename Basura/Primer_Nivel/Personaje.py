import pygame

def girar_imagen(lista_original,flip_x, flip_y):
    lista_girada= []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen,flip_x, flip_y))
    return lista_girada

def reescalar_imagenes(lista_animaciones, W, H):
    for lista in lista_animaciones:
        for i in range(len(lista)):
            imagen = lista[i]
            lista [i] = pygame.transform.scale(imagen,(W,H))


def actualizar_pantalla_daño (pantalla, personaje_vida,personaje_menos_una_vida, contador_daño):
    flag = True
    if contador_daño == 0:
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (80, 20))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (180, 20))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (280, 20))
    elif contador_daño == 1:
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (80, 20))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (180, 20))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (280, 20))
    elif contador_daño == 2:
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (80, 20))
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (180, 20))
        pantalla.blit(pygame.transform.scale(personaje_vida, (80, 80)), (280, 20))
    elif contador_daño == 3:
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (80, 20))
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (180, 20))
        pantalla.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (280, 20))
        flag = False
    return flag


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



personaje_quieto_izquierda = girar_imagen(personaje_quieto,True,False)
personaje_camina_izquierda = girar_imagen(personaje_camina,True,False)
personaje_corre_izquierda = girar_imagen(personaje_camina,True,False)
personaje_ataque_izquierda = girar_imagen(personaje_ataque, True, False)
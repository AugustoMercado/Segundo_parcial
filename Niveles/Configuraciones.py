import pygame

def girar_imagen(lista_original,flip_x, flip_y):
    lista_girada= []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen,flip_x, flip_y))
    return lista_girada

def reescalar_imagenes(lista_animaciones,tamaño):
    for i in range(len(lista_animaciones)):
        imagen = lista_animaciones[i]
        lista_animaciones[i] = pygame.transform.scale(imagen,tamaño)


def obtener_rectangulos(principal: pygame.Rect):
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 6)

    return diccionario



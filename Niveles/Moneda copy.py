import pygame
import random


def crear_moneda(x, y, item_vida):
    rectangulo_moneda = item_vida.get_rect()
    rectangulo_moneda.x=  x
    rectangulo_moneda.y = y
    diccionario_moneda = {}
    diccionario_moneda["superficie"] = item_moneda
    diccionario_moneda["rectangulo"] = rectangulo_moneda
    diccionario_moneda["velocidad"] = random.randrange(10,20,1)
    return diccionario_moneda
    
def crear_lista_monedas(W, cantidad, item_moneda):
    lista_monedas = []
    for i in range(cantidad):
        x = random.randrange(0, W, 50)
        y = random.randrange(700, 850, 50)
        moneda = crear_moneda(x,y,item_moneda)
        lista_monedas.append(moneda)
    return lista_monedas


def update (lista_monedas):
    for moneda in lista_monedas:
        rect = moneda ["rectangulo"]
        rect.y += moneda["velocidad"]

def desaparecer_moneda(rectangulo_moneda):
    rectangulo_moneda.x = -20
    rectangulo_moneda.y = -20
    
    
item_moneda  = [
    pygame.image.load("Recursos/item_moneda/11.png"),
    pygame.image.load("Recursos/item_moneda/12.png"),
    pygame.image.load("Recursos/item_moneda/13.png"),
    pygame.image.load("Recursos/item_moneda/14.png"),
    pygame.image.load("Recursos/item_moneda/15.png"),
    pygame.image.load("Recursos/item_moneda/16.png"),
    pygame.image.load("Recursos/item_moneda/17.png"),
    pygame.image.load("Recursos/item_moneda/18.png"),
    pygame.image.load("Recursos/item_moneda/19.png")
]
obtener_item_moneda = [
    pygame.image.load("Recursos/item_moneda/20.png"),
    pygame.image.load("Recursos/item_moneda/21.png")
]

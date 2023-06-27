import pygame
import random
from Niveles.Configuraciones import *
class Plataforma:
    def __init__(self,Path_image,tamaño,posicion):
        self.ancho = tamaño [0]
        self.alto = tamaño [1]
        self.plataforma = pygame.image.load(Path_image)
        self.base_plataforma = pygame.transform.scale(self.plataforma, (self.ancho,self.alto))     
        
        rectangulo = self.base_plataforma.get_rect()
        rectangulo.x = posicion[0]
        rectangulo.y =  posicion[1]
        self.lados_plataforma = obtener_rectangulos(rectangulo)
        
        
    def draw (self,pantalla):
        pantalla.blit(self.base_plataforma,self.lados_plataforma["main"])

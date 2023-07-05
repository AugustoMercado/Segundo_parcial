import pygame
import random
from Niveles.Configuraciones import *

class Objeto():
    def __init__(self,Path_image,tamaño,posicion_inicial) -> None:
            self.ancho = tamaño [0]
            self.alto = tamaño [1]
            
            self.Objeto = pygame.image.load(Path_image)
            self.Base_objeto = pygame.transform.scale(self.Objeto, (self.ancho,self.alto))    
            
            rectangulo_objeto = self.Base_objeto.get_rect()
            rectangulo_objeto.x = posicion_inicial[0]
            rectangulo_objeto.y =  posicion_inicial[1]
            self.lados_objeto = obtener_rectangulos(rectangulo_objeto)
    
    
    def draw (self,pantalla):
        pantalla.blit(self.Base_objeto,self.lados_objeto["main"])

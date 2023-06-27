import pygame
import random
from Niveles.Configuraciones import *
from Niveles.Class_Plataforma import *
from Niveles.Class_Personaje import Personaje
class Plataforma_trampa(Plataforma):
    def __init__(self,tamaño,posicion,animaciones):
        
        self.ancho = tamaño [0]
        self.alto = tamaño [1]
        self.contador_pasos = 0
        self.accion_trampa = " "
        self.animaciones = animaciones
        self.reescalar_animaciones()
        
        rectangulo = self.animaciones["Quieto"][0].get_rect()
        rectangulo.x = posicion[0]
        rectangulo.y =  posicion[1]
        self.lados_plataforma_trampa = obtener_rectangulos(rectangulo)
        
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho,self.alto))
        
    def draw (self,pantalla):
        pantalla.blit(self.animaciones,self.lados_plataforma_trampa["main"])
        

    def animar(self,pantalla,que_animacion: str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_pasos  >= largo:
            self.contador_pasos = 0
        pantalla.blit(animacion[self.contador_pasos],self.lados_plataforma_trampa["main"])
        self.contador_pasos += 1
        
    def update_plataforma(self,pantalla):
        match self.accion_trampa:
            case "Quieto":
                self.animar(pantalla,"Quieto")
            case "Ataque":
                self.animar(pantalla,"Ataque")
        
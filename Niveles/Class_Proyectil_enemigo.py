from Niveles.Modo import *
from Niveles.Class_Plataforma import *
from Niveles.Configuraciones import *
from Niveles.Enemigo import *
# from Niveles.Personaje import *
# from Niveles.Class_Personaje import Personaje

class Proyectil_enemigo():
    def __init__(self,tamaño,posicion_inicial,velocidad):
        self.ancho = tamaño [0]
        self.alto = tamaño [1]
        self.movimiento = 0
        self.velocidad = velocidad
        self.accion_kunai = " "
        self.kunai = personaje_kunai[0]
        self.animaciones = personaje_kunai
        rectangulo_proyectil =  self.kunai.get_rect()
        rectangulo_proyectil.x = posicion_inicial[0]
        rectangulo_proyectil.y =  posicion_inicial[1]
        self.lados_kunai = obtener_rectangulos(rectangulo_proyectil)
        # self.velocidad = velocidad

    def mover_proyectil(self,velocidad):
        self.lados_kunai["main"].x += velocidad
        

    def animar_kunai(self,pantalla,animacion: str):
        largo = len(animacion)
        
        if self.movimiento  >= largo:
            self.movimiento = 0
        pantalla.blit(animacion[self.movimiento],self.lados_kunai["main"])
        self.movimiento += 1
        

    def update_proyectil_kunai(self,pantalla):
        match self.accion_kunai:
            case "Ataque_derecha":
                self.mover_proyectil(self.velocidad)
                self.animar_kunai(pantalla, self.animaciones)
            case"Ataque_izquierda":
                self.mover_proyectil(self.velocidad * -1)
                self.animar_kunai(pantalla,  self.animaciones)
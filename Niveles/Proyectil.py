from Niveles.Modo import *
from Niveles.Class_Plataforma import *
from Niveles.Configuraciones import *
from Niveles.Personaje import *
# from Niveles.Personaje import *
# from Niveles.Class_Personaje import Personaje

class Proyectil():
    def __init__(self,tamaño,posicion_inicial,velocidad):
        self.ancho = tamaño [0]
        self.alto = tamaño [1]
        self.movimiento = 0
        self.velocidad = velocidad
        self.accion_flecha = " "
        self.flecha = Flecha[0]
        self.flecha_izq = Flecha_atras[0]
        
        rectangulo_proyectil =  self.flecha.get_rect()
        rectangulo_proyectil.x = posicion_inicial[0]
        rectangulo_proyectil.y =  posicion_inicial[1]
        self.lados_proyectil = obtener_rectangulos(rectangulo_proyectil)
        # self.velocidad = velocidad

    def mover_proyectil(self,velocidad):
        self.lados_proyectil["main"].x += velocidad
        

    def draw_arrow (self,pantalla,flecha):
        # self.plataforma.draw(pantalla)
        # pygame.draw.rect(flecha, "Red", self.lados_plataforma["main"] ,3)
        pantalla.blit(flecha,self.lados_proyectil["main"])
        

    def update_proyectil(self,pantalla):
        match self.accion_flecha:
            case "Ataque_derecha":
                self.mover_proyectil(self.velocidad)
                self.draw_arrow(pantalla,self.flecha)
            case"Ataque_izquierda":
                self.mover_proyectil(self.velocidad * -1)
                self.draw_arrow(pantalla,self.flecha_izq)
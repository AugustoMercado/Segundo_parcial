import pygame
from Niveles.Configuraciones import reescalar_imagenes,obtener_rectangulos
from Niveles.Proyectil import Proyectil
class Personaje:
    def __init__ (self, tamaño, animaciones, posicion_inicial,velocidad):
        self.ancho = tamaño [0]
        self.alto = tamaño [1]
        
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        
        self.contador_pasos = 0
        self.accion = "Quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        
        rectangulo = self.animaciones["Derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y =  posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho,self.alto))
            
    def animar(self,pantalla,que_animacion: str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_pasos  >= largo:
            self.contador_pasos = 0
        pantalla.blit(animacion[self.contador_pasos],self.lados["main"])
        self.contador_pasos += 1
        

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad
            
    def update(self,pantalla,plataformas):
        match self.accion:
            case "Quieto":
                if not self.esta_saltando:
                    self.animar(pantalla,"Quieto")
            case "Quieto izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla,"Quieto izquierda")
            case "Derecha":
                if not self.esta_saltando:
                    self.animar(pantalla,"Derecha")
                self.mover(self.velocidad)
            case "Izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla,"Izquierda")
                self.mover(self.velocidad*-1)
            case "Ataque":
                if not self.esta_saltando:
                    self.animar(pantalla,"Ataque")
                    Proyectil.accion_flecha = "Ataque_derecha"
            case "Ataque izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla,"Ataque izquierda")
                    Proyectil.accion_flecha = "Ataque_izquierda"
            case "Salta":
                    if not self.esta_saltando:
                        self.esta_saltando = True
                        self.desplazamiento_y = self.potencia_salto
                        self.animar(pantalla,"Salta")
                        self.mover(self.velocidad)
            case "Daño":
                if not self.esta_saltando:
                    pygame.mixer.init()
                    sonido_recolectar = pygame.mixer.Sound("Recursos/Sonidos/Sonido_Personaje.wav")
                    sonido_recolectar.set_volume(0.1)
                    sonido_recolectar.play()
                    self.animar(pantalla,"Daño")
        self.aplicar_graverdad(pantalla,plataformas)
    
    def aplicar_graverdad(self, pantalla,plataformas):
        if self.esta_saltando:
            self.animar(pantalla,"Salta")
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
                
        for piso in plataformas:
            if self.lados["bottom"].colliderect(piso["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = piso["main"].top + 5
                break
            else:
                self.esta_saltando = True
        
  
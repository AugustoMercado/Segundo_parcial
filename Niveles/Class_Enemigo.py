import pygame
from Niveles.Configuraciones import reescalar_imagenes,obtener_rectangulos

class Enemigo():
        def __init__ (self, tamaño, animaciones, posicion_inicial,muerto):
            self.ancho = tamaño [0]
            self.alto = tamaño [1]
            self.contador_pasos = 0
            self.accion_enemigo = " "
            
            self.gravedad = 1
            self.potencia_salto = -15
            self.limite_velocidad_caida = 15
            self.esta_saltando = False
            self.desplazamiento_y = 0
            self.muerto = muerto
                
            self.animaciones = animaciones
            self.reescalar_animaciones()
            
            rectangulo_enemigo = self.animaciones["Quieto izquierda"][0].get_rect()
            rectangulo_enemigo.x = posicion_inicial[0]
            rectangulo_enemigo.y =  posicion_inicial[1]
            self.lados_enemigo = obtener_rectangulos(rectangulo_enemigo)
            
            rectangulo_vision = self.animaciones["Ataque derecha"][0].get_rect()
            rectangulo_vision.x = rectangulo_enemigo.x - 250
            # rectangulo_vision.y = rectangulo_enemigo.y 
            rectangulo_vision.width = 600
            rectangulo_vision.height = 99
            self.lados_vision = obtener_rectangulos(rectangulo_vision)
        
        def reescalar_animaciones(self):
            for clave in self.animaciones:
                reescalar_imagenes(self.animaciones[clave], (self.ancho,self.alto))
                
                
        def animar_enemigo(self,pantalla,que_animacion: str):
            animacion = self.animaciones[que_animacion]
            largo = len(animacion)
            
            if self.contador_pasos  >= largo:
                self.contador_pasos = 0
            pantalla.blit(animacion[self.contador_pasos],self.lados_enemigo["main"])
            self.contador_pasos += 1
        
        def update_enemigo(self,pantalla,plataformas):
            if self.muerto == False:
                match self.accion_enemigo:
                    case "Quieto derecha":
                        self.animar_enemigo(pantalla,"Quieto")
                    case "Quieto izquierda":
                        self.animar_enemigo(pantalla,"Quieto izquierda")
                    case "Ataque derecha":
                        self.animar_enemigo(pantalla,"Ataque derecha")
                    case "Ataque izquierda":
                        self.animar_enemigo(pantalla,"Ataque izquierda")
                    case "Muerte":
                        self.animar_enemigo(pantalla,"Muerte")
                        pygame.mixer.init()
                        sonido_recolectar = pygame.mixer.Sound("Recursos/Sonidos/Sonido_Enemigo.wav")
                        sonido_recolectar.set_volume(0.1)
                        sonido_recolectar.play()
                self.aplicar_graverdad(plataformas)
            
            # self.animar_enemigo(pantalla,"Quieto")
            # self.animar_enemigo(pantalla,"Quieto izquierda")
            
        def aplicar_graverdad(self,plataformas):
            if self.esta_saltando:
                for lado in self.lados_enemigo:
                    self.lados_enemigo[lado].y += self.desplazamiento_y
                if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                    self.desplazamiento_y += self.gravedad
                    
            for piso in plataformas:
                if self.lados_enemigo["bottom"].colliderect(piso["top"]):
                    self.desplazamiento_y = 0
                    self.esta_saltando = False
                    self.lados_enemigo["main"].bottom = piso["main"].top + 5
                    break
                else:
                    self.esta_saltando = True


            
import pygame
from Niveles.Configuraciones import reescalar_imagenes,obtener_rectangulos

class Boss():
        def __init__ (self, tamaño, animaciones, posicion_inicial):
            self.ancho = tamaño [0]
            self.alto = tamaño [1]
            self.contador_pasos = 0
            self.accion_boss = " "
            self.boss_muerto = False
            
            self.gravedad = 1
            self.potencia_salto = -15
            self.limite_velocidad_caida = 15
            self.esta_saltando = False
            self.desplazamiento_y = 0
            
            self.animaciones = animaciones
            self.reescalar_animaciones()
            
            rectangulo_boss = self.animaciones["Quieto izquierda"][0].get_rect()
            rectangulo_boss.x = posicion_inicial[0]
            rectangulo_boss.y =  posicion_inicial[1]
            self.lados_boss = obtener_rectangulos(rectangulo_boss)
            
            rectangulo_vision_boss =  rectangulo_boss
            rectangulo_vision_boss.x = rectangulo_boss.x - 250
            rectangulo_vision_boss.y = rectangulo_boss.y 
            rectangulo_vision_boss.width = 100
            rectangulo_vision_boss.height = 100
            self.lados_vision_boss = obtener_rectangulos(rectangulo_vision_boss)
        
        def reescalar_animaciones(self):
            for clave in self.animaciones:
                reescalar_imagenes(self.animaciones[clave], (self.ancho,self.alto))
        
        def animar_boss(self,pantalla,que_animacion: str):
            animacion = self.animaciones[que_animacion]
            largo = len(animacion)
            
            if self.contador_pasos  >= largo:
                self.contador_pasos = 0
            pantalla.blit(animacion[self.contador_pasos],self.lados_boss["main"])
            self.contador_pasos += 1
        
        def update_boss(self,pantalla,plataformas):
            match self.accion_boss:
                case "Quieto_derecha":
                    self.animar_boss(pantalla,"Quieto")
                case "Quieto_izquierda":
                    self.animar_boss(pantalla,"Quieto izquierda")
                case "Ataque derecha":
                    pygame.mixer.init()
                    sonido_recolectar = pygame.mixer.Sound("Recursos/Sonidos/Hit_Espada.wav")
                    sonido_recolectar.set_volume(0.1)
                    sonido_recolectar.play()
                    self.animar_boss(pantalla,"Ataque")
                case "ataque izquierda":
                    pygame.mixer.init()
                    sonido_recolectar = pygame.mixer.Sound("Recursos/Sonidos/Hit_Espada.wav")
                    sonido_recolectar.set_volume(0.1)
                    sonido_recolectar.play()
                    self.animar_boss(pantalla,"ataque_izquierda")
                case "Muerte":
                    self.animar_boss(pantalla,"Muerte")
            self.aplicar_graverdad(plataformas)
            
        def aplicar_graverdad(self,plataformas):
            if self.esta_saltando:
                for lado in self.lados_boss:
                    self.lados_boss[lado].y += self.desplazamiento_y
                if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                    self.desplazamiento_y += self.gravedad
                    
            for piso in plataformas:
                if self.lados_boss["bottom"].colliderect(piso["top"]):
                    self.desplazamiento_y = 0
                    self.esta_saltando = False
                    self.lados_boss["main"].bottom = piso["main"].top + 5
                    break
                else:
                    self.esta_saltando = True

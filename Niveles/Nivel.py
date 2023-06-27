import pygame
import random
from Niveles.Modo import *
from Niveles.Moneda import *
from Niveles.Enemigo import * 
from Niveles.Proyectil import *
from Niveles.Personaje import *
from Niveles.Configuraciones import *
from Niveles.Class_Plataforma import *
from Niveles.Class_Personaje import *
from Niveles.Proyectil_enemigo import *
from Niveles.Class_Plataforma_Trampa import *
class Nivel:
    def __init__(self,pantalla,personaje_principal,lista_plataforma,diccionario_plataformas,imagen_fondo,Enemigo,kunai,arrow_,lista_monedas,lista_trampas):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataforma
        self.dicc_plataforma = diccionario_plataformas
        self.imagen_fondo = imagen_fondo
        self.puntaje = 0
        self.tiempo = 0
        self.tiempo_limite = 60
        self.enemigo = Enemigo
        # self.Vision = self.enemigo.lados.get_rect()
        self.kunai = kunai
        self.atacando_derecha = False
        self.atacando_izquierda = False
        self.mover_flecha_derecha = False
        self.mover_flecha_izquierda = False
        self.atacando_izquierda = 0 
        self.flecha = arrow_
        self.muerte = False
        self.contador_daño = 0
        self.contador_daño_enemigo = 0
        self.contador = 0
        self.fuerza = 50
        self.accion_moneda = item_moneda
        self.lista_monedas = lista_monedas
        self.contador_pasos_objeto = 0
        self.fuente = pygame.font.SysFont("ALGERIAN", 50)
        self.banner_time = pygame.image.load("Recursos/Tiempo/1.png")
        self.desaparecer = False
        
        self.lista_trampas = lista_trampas
        self.trampa_una = lista_trampas[0]
        self.trampa_dos = lista_trampas[1]
        self.trampa_tres = lista_trampas[2]
        self.activar_trampa_una = 0
        self.activar_trampa_dos = 0
        self.activar_trampa_tres = 0
        
        self.pocima = pocima
        self.pocima.x = 820
        self.pocima.y = 550
        self.lados_pocima = obtener_rectangulos(pocima)
        
        
        
    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                print(evento.pos)
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_TAB:
                cambiar_modo()
                
        self.dibujar_rectangulos()
        self.apretar_tecla()
        self.actualizar_pantalla ()
        self.ataque_enemigo()
        self.colision_moneda ()
        # self.update_trampa()
        self.detectar_colision_pocima()
        self.detectar_colisicion_flecha()
        self.detectar_colision_enemigo()
        self.detectar_colision_trampa()
        self.timer()
        self.actualizar_pantalla_daño()
        self.actualizar_uhi()
        self.End_game()

    def actualizar_pantalla (self):
        self._slave.blit(self.imagen_fondo,(0,0))
        
        for Plataforma in self.plataformas:
            Plataforma.draw(self._slave)
        for Trampa in self.lista_trampas:
            Trampa.update_plataforma(self._slave)  
            
        self.flecha.update_proyectil(self._slave)
        self.kunai.update_proyectil_kunai(self._slave)
        self.enemigo.update_enemigo(self._slave,self.dicc_plataforma)
        self.jugador.update(self._slave ,self.dicc_plataforma)
        
    def apretar_tecla(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT]):
            self.jugador.accion = "Derecha"
        elif keys[pygame.K_LEFT] and self.jugador.lados["main"].x > 0 - self.jugador.velocidad:
            self.jugador.accion = "Izquierda"
        elif keys[pygame.K_UP]:
            self.jugador.accion = "Salta"
        elif keys[pygame.K_k]:
            self.detectar_colisicion_flecha()
            pygame.mixer.init()
            sonido_recolectar = pygame.mixer.Sound("Recursos/Sonidos/Cargar_arco.wav")
            sonido_recolectar.set_volume(0.01)
            sonido_recolectar.play()
            if self.jugador.accion == "Izquierda":
                self.jugador.accion = "Ataque izquierda"
                self.mover_flecha_izquierda = True
                self.atacar()
            elif self.jugador.accion == "Derecha":
                self.jugador.accion = "Ataque"
                self.mover_flecha_derecha = True
                self.atacar()
            
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
        else:
            if self.jugador.accion == "izquierda":
                self.jugador.accion = "Quieto izquierda"
            elif self.jugador.accion == "Derecha":
                self.jugador.accion = "Quieto"
    
    def detectar_colision_trampa(self):

        if self.jugador.lados["main"].colliderect(self.trampa_una.lados_plataforma_trampa["top"]):
            if self.activar_trampa_una == 30:
                self.trampa_una.accion_trampa = "Ataque"
                self.contador_daño += 1
                self.jugador.accion = "Daño"
                self.activar_trampa_una = 0
            self.activar_trampa_una += 1
        else:
            self.trampa_una.accion_trampa = "Quieto"
            
        if self.jugador.lados["main"].colliderect(self.trampa_dos.lados_plataforma_trampa["top"]):
            if self.activar_trampa_dos == 30:
                self.trampa_dos.accion_trampa = "Ataque"
                self.contador_daño += 1
                self.jugador.accion = "Daño" 
                self.activar_trampa_dos = 0
            self.activar_trampa_dos += 1      
        else:
            self.trampa_dos.accion_trampa = "Quieto"
            
        if self.jugador.lados["main"].colliderect(self.trampa_tres.lados_plataforma_trampa["top"]):
            if self.activar_trampa_tres == 30:
                self.trampa_tres.accion_trampa = "Ataque"
                self.contador_daño += 1
                self.jugador.accion = "Daño" 
                self.activar_trampa_tres = 0
            self.activar_trampa_tres += 1
        else:
            self.trampa_tres.accion_trampa = "Quieto"
            
    def detectar_colision_pocima (self):
        self._slave.blit(item_especial,pocima)
        if self.jugador.lados["main"].colliderect(self.lados_pocima["main"]):
            desaparecer_moneda(self.lados_pocima["main"])
            self.fuerza += 100
    
                    
                
    def animar_objeto(self, accion_objeto, rectangulo_objeto):
        # self.contador_pasos_objeto = 0
        largo = len(accion_objeto)
        if self.contador_pasos_objeto >= largo:
            self.contador_pasos_objeto = 0
        self._slave.blit(accion_objeto[self.contador_pasos_objeto], rectangulo_objeto)
        self.contador_pasos_objeto += 1
    
    
    def colision_moneda (self):
        for moneda in self.lista_monedas:
            self.animar_objeto(item_moneda,moneda["rectangulo"])
            pygame.draw.rect(self._slave, "Black", moneda["rectangulo"], 2)
            if self.jugador.lados["main"].colliderect(moneda["rectangulo"]):
                pygame.mixer.init()
                sonido_recolectar = pygame.mixer.Sound("Moneda.mp3")
                sonido_recolectar.set_volume(0.1)
                sonido_recolectar.play()
                self.animar_objeto( obtener_item_moneda,moneda["rectangulo"])
                desaparecer_moneda(moneda["rectangulo"])
                self.puntaje += 50
    

    
    
    def detectar_colision_enemigo (self):
        if self.muerte == False:
            if self.enemigo.lados_enemigo["main"].x > self.jugador.lados["main"].x:
                if self.enemigo.lados_vision["main"].colliderect(self.jugador.lados["main"]):
                    self.enemigo.accion_enemigo = "Ataque izquierda"
                    self.atacando_izquierda = True
                    self.ataque_enemigo()
                else:
                    self.enemigo.accion_enemigo = "Quieto izquierda"
            elif self.enemigo.lados_enemigo["main"].x < self.jugador.lados["main"].x:
                if self.enemigo.lados_vision["main"].colliderect(self.jugador.lados["main"]):
                    self.enemigo.accion_enemigo = "Ataque derecha"
                    self.atacando_derecha = True
                    self.ataque_enemigo()
                else:
                    self.enemigo.accion_enemigo = "Quieto derecha"
        else:
            self.enemigo.accion_enemigo = " "
            # self.enemigo.desplazamiento_y = 1000
            

    def atacar(self):
        if self.mover_flecha_derecha == True:
            self.flecha.accion_flecha =  "Ataque_derecha"
            pygame.mixer.init()
            sonido_recolectar = pygame.mixer.Sound("Recursos/Sonidos/Disparar_flecha.wav")
            sonido_recolectar.set_volume(0.1)
            sonido_recolectar.play()
            self.mover_flecha_derecha = False
        elif self.mover_flecha_izquierda == True:
            self.flecha.accion_flecha =  "Ataque_izquierda"
            self.mover_flecha_izquierda = False
            pygame.mixer.init()
            sonido_recolectar = pygame.mixer.Sound("Recursos/Sonidos/Disparar_flecha.wav")
            sonido_recolectar.set_volume(0.1)
            sonido_recolectar.play()
        self.detectar_colisicion_flecha()
        
    def ataque_enemigo(self):
        if self.atacando_derecha == True:
            self.kunai.accion_kunai = "Ataque_derecha"
            self.atacando_derecha = False
            
        elif self.atacando_izquierda  == True:
            self.kunai.accion_kunai = "Ataque_izquierda"
            self.atacando_izquierda = False
        self.detectar_coliccion_kunai()
    
    
    def detectar_colisicion_flecha(self):
        if self.flecha.lados_proyectil["main"].x > self._slave.get_width() + 100:
            self.desaparecer_flecha()
        elif self.flecha.lados_proyectil["main"].x < 0:
            self.desaparecer_flecha()
        elif self.flecha.lados_proyectil["main"].colliderect(self.enemigo.lados_enemigo["main"]):
            self.contador_daño_enemigo += 1
            self.enemigo.accion_enemigo = "Muerte"
            self.desaparecer_flecha()
            if self.contador_daño_enemigo == 2:
                self.muerte = True
                self.puntaje += 100
            pygame.mixer.init()
            sonido_recolectar = pygame.mixer.Sound("Recursos/Sonidos/Flecha_hit.wav")
            sonido_recolectar.set_volume(0.1)
            sonido_recolectar.play()
        


                
    def detectar_coliccion_kunai(self):
        if self.muerte != True:
            if self.kunai.lados_kunai["main"].x > self._slave.get_width() + 100:
                self.desaparecer_kunai()
            elif self.kunai.lados_kunai["main"].x < 0:
                self.desaparecer_kunai()
            elif self.kunai.lados_kunai["main"].colliderect(self.jugador.lados["main"]):
                self.jugador.accion = "Daño"
                self.contador_daño += 0.5
                self.desaparecer_kunai()
                pygame.mixer.init()
                sonido_recolectar = pygame.mixer.Sound("Recursos/Sonidos/Flecha_hit.wav")
                sonido_recolectar.set_volume(0.1)
                sonido_recolectar.play()
                    
    
    def desaparecer_kunai(self):
        self.kunai.accion_kunai =  " " 
        self.kunai.lados_kunai["main"].x = self.enemigo.lados_enemigo["main"].x + 5
        self.kunai.lados_kunai["main"].y = self.enemigo.lados_enemigo["main"].y + 30
        
    def desaparecer_flecha(self):
        self.flecha.accion_flecha =  " " 
        self.flecha.lados_proyectil["main"].x = self.jugador.lados["main"].x + 5
        self.flecha.lados_proyectil["main"].y = self.jugador.lados["main"].y + 30
        
    
    def dibujar_rectangulos(self):        
        if get_modo():
            for lado in  self.jugador.lados:
                pygame.draw.rect(self._slave, "Red",  self.jugador.lados[lado],3)
                
            for plataforma in self.plataformas:
                for lado in plataforma.lados_plataforma:
                    pygame.draw.rect(self._slave, "Red", plataforma.lados_plataforma[lado],3)

    def End_game(self):
        if self.jugador.lados["main"].x > self._slave.get_width() + 100 or self.jugador.lados["main"].y > self._slave.get_height() + 100:
            self.puntaje += self.tiempo_limite
            print(self.puntaje)
            pygame.quit()
            
        elif self.jugador.lados["main"].y > self._slave.get_height() + 100:
            pygame.quit()
    def timer(self):
        self.contador += 1
        if  self.contador == 15:     
            if self.tiempo != self.tiempo_limite:
                self.tiempo_limite -= 1
                self.contador = 0
            else:
                self.tiempo_limite = 0
                pygame.quit()
            
        
    def actualizar_pantalla_daño (self):
        if self.contador_daño == 0:
            self._slave.blit(pygame.transform.scale(personaje_vida, (80, 80)), (80, 20))
            self._slave.blit(pygame.transform.scale(personaje_vida, (80, 80)), (180, 20))
            self._slave.blit(pygame.transform.scale(personaje_vida, (80, 80)), (280, 20))
        elif self.contador_daño == 1:
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (80, 20))
            self._slave.blit(pygame.transform.scale(personaje_vida, (80, 80)), (180, 20))
            self._slave.blit(pygame.transform.scale(personaje_vida, (80, 80)), (280, 20))
        elif self.contador_daño == 2:
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (80, 20))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (180, 20))
            self._slave.blit(pygame.transform.scale(personaje_vida, (80, 80)), (280, 20))
        elif self.contador_daño == 3:
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (80, 20))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (180, 20))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (280, 20))
            pygame.quit()

    def actualizar_uhi(self):
            tiempo = self.fuente.render(":{0}".format(self.tiempo_limite), True, [255, 255, 255])
            score = self.fuente.render("Score:{0}".format(self.puntaje), True, [255, 255, 255])
            stronght = self.fuente.render("Fuerza:{0}".format(self.fuerza), True, [255, 255, 255])
            self._slave.blit(pygame.transform.scale(self.banner_time, (80, 50)), (self._slave.get_width() / 2 - 30, 10))
            self._slave.blit(tiempo, (self._slave.get_width() / 2 + 50, 10))
            self._slave.blit(score, (self._slave.get_width() / 2 + 400, 10))
            self._slave.blit(stronght, (self._slave.get_width() / 2 + 400, 50))

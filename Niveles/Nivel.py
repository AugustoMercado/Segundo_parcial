import pygame, sys
import random
from Niveles.Modo import *
from Niveles.Boss import *
from Niveles.Moneda import *
from Niveles.Enemigo import *
from Niveles.Class_Proyectil import *
from Niveles.Personaje import *
from Niveles.Configuraciones import *
from Niveles.Class_Plataforma import *
from Niveles.Class_Personaje import *
from Niveles.Class_Proyectil_enemigo import *
from Niveles.Class_Plataforma_Trampa import *


class Nivel:
    def __init__(self,pantalla,personaje_principal,lista_plataforma,diccionario_plataformas,imagen_fondo,
        lista_enemigos,lista_kunais,arrow_,lista_monedas,lista_items_a_recolectar_,lista_trampas=any,mi_boss=any,):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.posicion_actual_x = 0
        self.posicion_actual_y = 0

        self.plataformas = lista_plataforma
        self.dicc_plataforma = diccionario_plataformas

        self.imagen_fondo = imagen_fondo
        self.puntaje = 0
        self.tiempo = 0
        self.tiempo_limite = 60

        self.lista_enemigos = lista_enemigos
        self.lista_kunais = lista_kunais
        self.atacando_derecha = False
        self.atacando_izquierda = False
        self.boss = mi_boss
        self.contador_daño_boss = 0
        self.muerte_boss = False
        self.ataque_derecha_boss = False
        self.ataque_izquierda_boss = False
        self.mover_flecha_derecha = False
        self.mover_flecha_izquierda = False

        self.flecha = arrow_
        self.muerte = 0
        self.contador_daño = 0
        self.contador_daño_enemigo = 0
        self.contador = 0
        self.fuerza = 50
        self.accion_moneda = item_moneda
        self.lista_monedas = lista_monedas
        self.contador_pasos_objeto = 0
        self.lista_de_trampas = lista_trampas
        self.activar_trampa_una = 0
        self.activar_trampa_dos = 0
        self.activar_trampa_tres = 0
        self.fuente = pygame.font.SysFont("ALGERIAN", 50)
        self.banner_time = pygame.image.load("Recursos/Tiempo/1.png")
        self.desaparecer = False
        self.teletransporte = 0
        self.lista_items_a_recolectar_ = lista_items_a_recolectar_

        self.pocima_fuerza = self.lista_items_a_recolectar_[0]

        self.lista_pocimas_vida = []
        self.pocima_vida = self.lista_items_a_recolectar_[1]
        self.lista_pocimas_vida.append(self.pocima_vida)
        self.pocima_vida_dos = self.lista_items_a_recolectar_[2]
        self.lista_pocimas_vida.append(self.pocima_vida_dos)
        self.pocima_vida_tres = self.lista_items_a_recolectar_[3]
        self.lista_pocimas_vida.append(self.pocima_vida_tres)

        if self.lista_de_trampas != any:
            self.trampa_una = self.lista_de_trampas[0]
            self.trampa_dos = self.lista_de_trampas[1]
            self.trampa_tres = self.lista_de_trampas[2]

    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                print(evento.pos)
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_TAB:
                cambiar_modo()

        self.apretar_tecla()
        self.actualizar_pantalla()
        self.colision_moneda()
        self.detectar_colision_Boss()
        self.aparecer_pocimas_vida()
        self.detectar_colision_pocima_fuerza()
        self.detectar_colision_pocima_vida()
        self.detectar_colision_enemigo()
        self.detectar_colisicion_flecha()
        self.detectar_colision_trampa()
        self.actualizar_pantalla_daño()
        self.aparecer_pocimas_vida()
        self.actualizar_uhi()
        self.timer()
        self.End_game()

    def reiniciar_nivel(self):
        self.__init__(self._slave)

    def actualizar_pantalla(self):
        self._slave.blit(self.imagen_fondo, (0, 0))

        for platform in self.plataformas:
            platform.draw(self._slave)

        if self.lista_de_trampas != any:
            for trampa in self.lista_de_trampas:
                trampa.update_plataforma(self._slave)

        for enemigo in self.lista_enemigos:
            enemigo.update_enemigo(self._slave, self.dicc_plataforma)

        for kunai in self.lista_kunais:
            kunai.update_proyectil_kunai(self._slave)

        if self.boss != any:
            self.teletransportar_boss()
            self.boss.update_boss(self._slave, self.dicc_plataforma)
            self.actualizar_pantalla_daño_boss()
        self.flecha.update_proyectil(self._slave)
        self.jugador.update(self._slave, self.dicc_plataforma)

    def apretar_tecla(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.jugador.accion = "Derecha"
        elif (
            keys[pygame.K_LEFT]
            and self.jugador.lados["main"].x > 0 - self.jugador.velocidad
        ):
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
                self.posicion_actual_x = self.jugador.lados["main"].x
                self.posicion_actual_y = self.jugador.lados["main"].y
                self.atacar()
            elif self.jugador.accion == "Derecha":
                self.jugador.accion = "Ataque"
                self.mover_flecha_derecha = True
                self.posicion_actual_x = self.jugador.lados["main"].x
                self.posicion_actual_y = self.jugador.lados["main"].y
                self.atacar()
        elif keys[pygame.K_r]:
            self.reiniciar_nivel()
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
        else:
            if self.jugador.accion == "izquierda":
                self.jugador.accion = "Quieto izquierda"
            elif self.jugador.accion == "Derecha":
                self.jugador.accion = "Quieto"

    def detectar_colision_trampa(self):
        if self.lista_de_trampas != any:
            if self.jugador.lados["main"].colliderect(
                self.trampa_una.lados_plataforma_trampa["top"]
            ):
                if self.activar_trampa_una == 30:
                    self.trampa_una.accion_trampa = "Ataque"
                    self.contador_daño += 1
                    self.jugador.accion = "Daño"
                    self.activar_trampa_una = 0
                self.activar_trampa_una += 1
            else:
                self.trampa_una.accion_trampa = "Quieto"

            if self.jugador.lados["main"].colliderect(
                self.trampa_dos.lados_plataforma_trampa["top"]
            ):
                if self.activar_trampa_dos == 30:
                    self.trampa_dos.accion_trampa = "Ataque"
                    self.contador_daño += 1
                    self.jugador.accion = "Daño"
                    self.activar_trampa_dos = 0
                self.activar_trampa_dos += 1
            else:
                self.trampa_dos.accion_trampa = "Quieto"

            if self.jugador.lados["main"].colliderect(
                self.trampa_tres.lados_plataforma_trampa["top"]
            ):
                if self.activar_trampa_tres == 30:
                    self.trampa_tres.accion_trampa = "Ataque"
                    self.contador_daño += 1
                    self.jugador.accion = "Daño"
                    self.activar_trampa_tres = 0
                self.activar_trampa_tres += 1
            else:
                self.trampa_tres.accion_trampa = "Quieto"

    def detectar_colision_pocima_fuerza(self):
        self.pocima_fuerza.draw(self._slave)
        if self.jugador.lados["main"].colliderect(
            self.pocima_fuerza.lados_objeto["main"]):
            pygame.mixer.init()
            sonido_recolectar = pygame.mixer.Sound("Recursos/Sonidos/recolectar.mp3")
            sonido_recolectar.set_volume(0.1)
            sonido_recolectar.play()
            desaparecer_moneda(self.pocima_fuerza.lados_objeto["main"])
            self.fuerza += 100

    def aparecer_pocimas_vida(self):
        if self.contador_daño > 0:
            for pocima in self.lista_pocimas_vida:
                pocima.draw(self._slave)

    def detectar_colision_pocima_vida(self):
        for pocima in self.lista_pocimas_vida:
            if self.contador_daño > 0:
                if self.jugador.lados["main"].colliderect(pocima.lados_objeto["main"]):
                    pygame.mixer.init()
                    sonido_recolectar = pygame.mixer.Sound("Recursos/Sonidos/recolectar.mp3")
                    sonido_recolectar.set_volume(0.1)
                    sonido_recolectar.play()
                    desaparecer_moneda(pocima.lados_objeto["main"])
                    self.contador_daño -= 1

    def animar_objeto(self, accion_objeto, rectangulo_objeto):
        largo = len(accion_objeto)
        if self.contador_pasos_objeto >= largo:
            self.contador_pasos_objeto = 0
        self._slave.blit(accion_objeto[self.contador_pasos_objeto], rectangulo_objeto)
        self.contador_pasos_objeto += 1

    def colision_moneda(self):
        for moneda in self.lista_monedas:
            self.animar_objeto(item_moneda, moneda["rectangulo"])
            pygame.draw.rect(self._slave, "Black", moneda["rectangulo"], 2)
            if self.jugador.lados["main"].colliderect(moneda["rectangulo"]):
                pygame.mixer.init()
                sonido_recolectar = pygame.mixer.Sound("Moneda.mp3")
                sonido_recolectar.set_volume(0.1)
                sonido_recolectar.play()
                self.animar_objeto(obtener_item_moneda, moneda["rectangulo"])
                desaparecer_moneda(moneda["rectangulo"])
                self.puntaje += 50

    def detectar_colision_enemigo(self):
        for enemigo in self.lista_enemigos:
            if enemigo.muerto != True:
                enemigo.lados_vision["main"].y = enemigo.lados_enemigo["main"].y
                for kunai in self.lista_kunais:
                    if self.muerte < 4:
                        if enemigo.lados_enemigo["main"].x > self.jugador.lados["main"].x:
                            if enemigo.lados_vision["main"].colliderect(
                                self.jugador.lados["main"]):
                                enemigo.accion_enemigo = "Ataque izquierda"
                                self.atacando_izquierda = True
                                self.ataque_enemigo(kunai, enemigo)
                            else:
                                enemigo.accion_enemigo = "Quieto izquierda"
                        elif enemigo.lados_enemigo["main"].x < self.jugador.lados["main"].x:
                            if enemigo.lados_vision["main"].colliderect(
                                self.jugador.lados["main"]):
                                enemigo.accion_enemigo = "Ataque derecha"
                                self.atacando_derecha = True
                                self.ataque_enemigo(kunai, enemigo)
                            else:
                                enemigo.accion_enemigo = "Quieto derecha"
                    else:
                        if enemigo.muerto == True:
                            enemigo.accion_enemigo = " "
                            enemigo.desplazamiento_y = 1000

    def detectar_colision_Boss(self):
        if self.boss != any:
            if self.muerte_boss == False:
                if self.boss.lados_boss["main"].x > self.jugador.lados["main"].x:
                    if self.boss.lados_vision_boss["main"].colliderect(
                        self.jugador.lados["main"]):
                        self.boss.accion_boss = "Ataque_uno_izquierda"
                        self.jugador.accion = "Daño"
                        self.contador_daño += 0.2
                    else:
                        self.boss.accion_boss = "Quieto_izquierda"

                elif self.boss.lados_boss["main"].x < self.jugador.lados["main"].x:
                    if self.boss.lados_vision_boss["main"].colliderect(
                        self.jugador.lados["main"]):
                        self.boss.accion_boss = "Ataque_uno"
                        self.jugador.accion = "Daño"
                        self.contador_daño += 0.1
                    else:
                        self.boss.accion_boss = "Quieto_derecha"
            else:
                if self.contador_daño_boss == 12:
                    self.puntaje += 1000
                    self.boss.accion_boss = " "

    def atacar(self):
        if self.mover_flecha_derecha == True:
            self.flecha.accion_flecha = "Ataque_derecha"
            pygame.mixer.init()
            sonido_recolectar = pygame.mixer.Sound(
            "Recursos/Sonidos/Disparar_flecha.wav")
            sonido_recolectar.set_volume(0.1)
            sonido_recolectar.play()
            self.mover_flecha_derecha = False
        elif self.mover_flecha_izquierda == True:
            self.flecha.accion_flecha = "Ataque_izquierda"
            self.mover_flecha_izquierda = False
            pygame.mixer.init()
            sonido_recolectar = pygame.mixer.Sound(
            "Recursos/Sonidos/Disparar_flecha.wav")
            sonido_recolectar.set_volume(0.1)
            sonido_recolectar.play()
        self.flecha.lados_proyectil["main"].x = self.posicion_actual_x + 25
        self.flecha.lados_proyectil["main"].y = self.posicion_actual_y + 43
        self.detectar_colisicion_flecha()

    def ataque_enemigo(self, kunai, enemigo):
        for kunai in self.lista_kunais:
            if self.atacando_derecha == True:
                kunai.accion_kunai = "Ataque_derecha"
                self.atacando_derecha = False

            elif self.atacando_izquierda == True:
                kunai.accion_kunai = "Ataque_izquierda"
                self.atacando_izquierda = False
            self.detectar_coliccion_kunai(kunai, enemigo)

    def teletransportar_boss(self):
        if self.muerte_boss != True:
            if self.contador == 10:
                self.teletransporte += 1
                if self.teletransporte == 10:
                    self.boss.lados_boss["main"].x = self.jugador.lados["main"].x - 10
                    self.boss.lados_boss["main"].x = self.boss.lados_vision_boss["main"].x
                    self.teletransporte = 0

    def detectar_colisicion_flecha(self):
        if self.flecha.lados_proyectil["main"].x > self._slave.get_width() + 100:
            self.desaparecer_flecha()
        elif self.flecha.lados_proyectil["main"].x < 0:
            self.desaparecer_flecha()
        elif self.boss != any:
            if self.flecha.lados_proyectil["main"].colliderect(
                self.boss.lados_boss["main"]):
                if self.fuerza > 100:
                    self.contador_daño_boss += 2
                else:
                    self.contador_daño_boss += 1
                self.boss.accion_boss = "Muerte"
                self.desaparecer_flecha()
                pygame.mixer.init()
                sonido_recolectar = pygame.mixer.Sound(
                "Recursos/Sonidos/Flecha_hit.wav")
                sonido_recolectar.set_volume(0.1)
                sonido_recolectar.play()

        for enemigo in self.lista_enemigos:
            if enemigo.muerto != True:
                if self.flecha.lados_proyectil["main"].colliderect(
                    enemigo.lados_enemigo["main"]):
                    self.desaparecer_flecha()
                    self.contador_daño_enemigo += 1
                    enemigo.accion_enemigo = "Muerte"
                    if self.contador_daño_enemigo == 2:
                        self.contador_daño_enemigo = 0
                        self.muerte += 1
                        self.puntaje += 100
                        enemigo.muerto = True
                        if enemigo.muerto == True:
                            enemigo.desplazamiento_y = 50
                        pygame.mixer.init()
                        sonido_recolectar = pygame.mixer.Sound(
                        "Recursos/Sonidos/Flecha_hit.wav")
                        sonido_recolectar.set_volume(0.1)
                        sonido_recolectar.play()

        for plataforma in self.plataformas:
            if self.flecha.lados_proyectil["main"].colliderect(
                plataforma.lados_plataforma["main"]):
                pygame.mixer.init()
                sonido_recolectar = pygame.mixer.Sound(
                "Recursos/Sonidos/Flecha_hit.wav")
                sonido_recolectar.set_volume(0.1)
                sonido_recolectar.play()
                self.desaparecer_flecha()

    def detectar_coliccion_kunai(self, kunai, enemigo):
        if kunai.lados_kunai["main"].x > self._slave.get_width() + 100:
            self.desaparecer_kunai(kunai, enemigo)
        elif kunai.lados_kunai["main"].x < 0:
            self.desaparecer_kunai(kunai, enemigo)
        elif kunai.lados_kunai["main"].colliderect(self.jugador.lados["main"]):
            self.jugador.accion = "Daño"
            self.contador_daño += 0.5
            self.desaparecer_kunai(kunai, enemigo)
            pygame.mixer.init()
            sonido_recolectar = pygame.mixer.Sound("Recursos/Sonidos/Flecha_hit.wav")
            sonido_recolectar.set_volume(0.1)
            sonido_recolectar.play()

    def desaparecer_kunai(self, kunai, enemigo):
        kunai.accion_kunai = " "
        kunai.lados_kunai["main"].x = enemigo.lados_enemigo["main"].x + 5
        kunai.lados_kunai["main"].y = enemigo.lados_enemigo["main"].y + 30

    def desaparecer_flecha(self):
        self.flecha.accion_flecha = " "
        self.flecha.lados_proyectil["main"].x = self.posicion_actual_x + 5
        self.flecha.lados_proyectil["main"].y = self.posicion_actual_y + 30


    def End_game(self):
        if self.jugador.lados["main"].x > self._slave.get_width() + 100:
            self.puntaje += self.tiempo_limite
            pygame.quit()
        elif (self.jugador.lados["main"].y > self._slave.get_height() + 100
            or self.contador_daño == 5):
            self.reiniciar_nivel()

    def timer(self):
        self.contador += 1
        if self.contador == 15:
            if self.tiempo != self.tiempo_limite:
                self.tiempo_limite -= 1
                self.contador = 0
            else:
                self.tiempo_limite = 0
                self.reiniciar_nivel()
                
    def actualizar_pantalla_daño(self):
        if self.contador_daño >= 0 or self.contador_daño == 1:
            self._slave.blit(pygame.transform.scale(personaje_vida,
                                                    (80, 80)), (80, 20))
            self._slave.blit(pygame.transform.scale(personaje_vida,
                                                    (80, 80)), (180, 20))
            self._slave.blit(pygame.transform.scale(personaje_vida,
                                                    (80, 80)), (280, 20))
        elif self.contador_daño <= 1.5 or self.contador_daño == 2:
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (80, 20))
            self._slave.blit(pygame.transform.scale(personaje_vida,
                                                    (80, 80)), (180, 20))
            self._slave.blit(pygame.transform.scale(personaje_vida,
                                                    (80, 80)), (280, 20))
        elif self.contador_daño <= 2.5 or self.contador_daño == 3:
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (80, 20))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (180, 20))
            self._slave.blit(pygame.transform.scale(personaje_vida,
                                                    (80, 80)), (280, 20))
        elif self.contador_daño <= 3.5 or self.contador_daño > 4:
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida, 
                                                    (80, 80)), (80, 20))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida, 
                                                    (80, 80)), (180, 20))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida, 
                                                    (80, 80)), (280, 20))
            self.reiniciar_nivel()

    def actualizar_pantalla_daño_boss(self):
        self.muerte_boos = False
        if self.contador_daño_boss <= 1:
            self._slave.blit(pygame.transform.scale(vida_boos, (80, 80)), (1000, 100))
            self._slave.blit(pygame.transform.scale(vida_boos, (80, 80)), (1100, 100))
            self._slave.blit(pygame.transform.scale(vida_boos, (80, 80)), (1200, 100))
            self._slave.blit(pygame.transform.scale(vida_boos, (80, 80)), (1300, 100))
            self._slave.blit(pygame.transform.scale(vida_boos, (80, 80)), (1400, 100))
        elif self.contador_daño_boss > 1 and self.contador_daño_boss <= 3:
            self._slave.blit(
            pygame.transform.scale(personaje_menos_una_vida, (80, 80)), (1000, 100))
            self._slave.blit(pygame.transform.scale(vida_boos, (80, 80)), (1100, 100))
            self._slave.blit(pygame.transform.scale(vida_boos, (80, 80)), (1200, 100))
            self._slave.blit(pygame.transform.scale(vida_boos, (80, 80)), (1300, 100))
            self._slave.blit(pygame.transform.scale(vida_boos, (80, 80)), (1400, 100))
        elif self.contador_daño_boss > 3 and self.contador_daño_boss <= 6:
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (1000, 100))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (1100, 100))
            self._slave.blit(pygame.transform.scale(vida_boos, 
                                                    (80, 80)), (1200, 100))
            self._slave.blit(pygame.transform.scale(vida_boos, 
                                                    (80, 80)), (1300, 100))
            self._slave.blit(pygame.transform.scale(vida_boos, 
                                                    (80, 80)), (1400, 100))
        elif self.contador_daño_boss > 6 and self.contador_daño_boss <= 9:
            self._slave.blit(
            pygame.transform.scale(personaje_menos_una_vida,
                                (80, 80)), (1000, 100))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                            (80, 80)), (1100, 100))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (1200, 100))
            self._slave.blit(pygame.transform.scale(vida_boos,
                                                    (80, 80)), (1300, 100))
            self._slave.blit(pygame.transform.scale(vida_boos,
                                                    (80, 80)), (1400, 100))
        elif self.contador_daño_boss > 9 and self.contador_daño_boss <= 11:
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (1000, 100))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (1100, 100))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (1200, 100))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (1300, 100))
            self._slave.blit(pygame.transform.scale(vida_boos,
                                                    (80, 80)), (1400, 100))
        elif self.contador_daño_boss == 12:
            self._slave.blit(
            pygame.transform.scale(personaje_menos_una_vida,
                                (80, 80)), (1000, 100))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (1100, 100))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (1200, 100))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (1300, 100))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (1400, 100))
            self._slave.blit(pygame.transform.scale(personaje_menos_una_vida,
                                                    (80, 80)), (280, 20))
            self.muerte_boos = True

    def actualizar_uhi(self):
        tiempo = self.fuente.render(
        ":{0}".format(self.tiempo_limite), True, [255, 255, 255])
        score = self.fuente.render(
        "Score:{0}".format(self.puntaje), True, [255, 255, 255])
        stronght = self.fuente.render(
        "Fuerza:{0}".format(self.fuerza), True, [255, 255, 255])
        self._slave.blit(
        pygame.transform.scale(self.banner_time, (80, 50)),
        (self._slave.get_width() / 2 - 30, 10),)
        self._slave.blit(tiempo, (self._slave.get_width() / 2 + 50, 10))
        self._slave.blit(score, (self._slave.get_width() / 2 + 400, 10))
        self._slave.blit(stronght, (self._slave.get_width() / 2 + 400, 50))

    # def dibujar_rectangulos(self):
    #     if get_modo():
    #         for lado in self.jugador.lados:
    #             pygame.draw.rect(self._slave, "Red", self.jugador.lados[lado], 3)

    #         for plataforma in self.plataformas:
    #             for lado in plataforma.lados_plataforma:
    #                 pygame.draw.rect(self._slave, "Red", plataforma.lados_plataforma[lado], 3)

    #         pygame.draw.rect(self._slave, "Blue", self.boss.lados_boss["main"], 10)
    #         pygame.draw.rect(self._slave, "Red", self.boss.lados_vision_boss["main"], 2)
    
            # self.dibujar_rectangulos()

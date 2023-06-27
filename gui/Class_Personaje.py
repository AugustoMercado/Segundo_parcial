import pygame
from Niveles.Personaje import *

class Personaje:
    def __init__(self,velocidad,cantidad_pasos,potencia_salto, path_animaciones, widht, height, tipo_personaje, margen_x, margen_y ):
        self._tipo_personaje = tipo_personaje
        self._path_animaciones = path_animaciones
        self._contador_animaciones = 0
        self._potencia_salto = potencia_salto
        self._velocidad = velocidad
        self._cantidad_pasos = cantidad_pasos
        self._widht = widht
        self._height = height
        self._margen_x = margen_x
        self._margen_y = margen_y

    def mover_personaje(rectangulo_personaje: pygame.Rect, velocidad):
        for lado in rectangulo_personaje:
            rectangulo_personaje[lado].x += velocidad
            
    def update_personaje(self,pantalla, path_animaciones, lados_personaje, velocidad, plataformas):
    # pantalla.blit(fondo, (0, 0))
    # pantalla.blit(plataforma, (rectangulo_plataforma.x, rectangulo_plataforma.y))
        match path_animaciones:
            case "Derecha":
                    animar(pantalla, lados_personaje["main"], personaje_camina)
                    mover_personaje(lados_personaje, velocidad)
            case "Izquierda":
                    animar(pantalla, lados_personaje["main"], personaje_camina_izquierda)
                    mover_personaje(lados_personaje, velocidad * -1)
            case "Ataque":
                if not esta_saltando:
                    animar(pantalla, lados_personaje["main"], personaje_ataque)
            case "Ataque izquierda":
                if not esta_saltando:
                    animar(pantalla, lados_personaje["main"], personaje_ataque)
            case "Salta":
                if not esta_saltando:
                    esta_saltando = True
                    desplazamiento_y = potencia_salto
                    animar(pantalla, lados_personaje["main"], personaje_salta)
            case "Quieto":
                if not esta_saltando:
                    animar(pantalla, lados_personaje["main"], personaje_quieto)
            case "Quieto izquierda":
                if not esta_saltando:
                    animar(pantalla, lados_personaje["main"], personaje_quieto_izquierda)
            case "Daño":
                if not esta_saltando:
                    animar(pantalla, lados_personaje["main"], personaje_daño)
        # aplicar_gravedad(pantalla, personaje_salta, lados_personaje, plataformas)


    # def animar(self,pantalla):
    #     largo = len(self._path_animaciones)
    #     if self._cantidad_pasos >= largo:
    #         self._cantidad_pasos = 0
    #     pantalla.blit(self._path_animaciones[self._cantidad_pasos], self._rects)
    #     self._cantidad_pasos += 1

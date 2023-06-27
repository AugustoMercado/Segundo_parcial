import pygame

from Niveles.Personaje import *
from Niveles.Configuraciones import *
from Niveles.Class_Personaje import *
from Niveles.Class_Plataforma import Plataforma
from Niveles.Class_Enemigo import Enemigo
from Niveles.Nivel import Nivel
from Niveles.Nivel_dos import *
from Niveles.Modo import *
from Niveles.Enemigo import *
from Niveles.Proyectil import *
from Niveles.Proyectil_enemigo import *
from Niveles.Moneda import *

class Nivel_uno(Nivel):
    def __init__(self,pantalla:pygame.Surface):
        
        W = pantalla.get_width()
        H = pantalla.get_height()
        
        # FONDO
        fondo = pygame.image.load("Recursos/Fondo/1er Nivel.jpg")
        fondo = pygame.transform.scale(fondo, (W, H))
        # # Tiempo
        time = 5
        banner_time = pygame.image.load("Recursos/Tiempo/1.png")
        # # Fuente
        # fuente = pygame.font.SysFont("ALGERIAN", 50)
        score = 0
        ########################################################################################################
        # PERSONAJE
        tamaño = (70,85)
        posicion_incial = (W / 2 - 500,790)
        velocidad = 5
        animaciones = {}
        animaciones["Quieto"] = personaje_quieto
        animaciones["Quieto izquierda"] = personaje_quieto_izquierda
        animaciones["Derecha"] = personaje_camina
        animaciones["Izquierda"] = personaje_camina_izquierda
        animaciones["Ataque"] = personaje_ataque
        animaciones["Ataque izquierda"] = personaje_ataque_izquierda
        animaciones["Salta"] = personaje_salta
        animaciones["Daño"] = personaje_daño
        mi_personaje = Personaje(tamaño,animaciones,posicion_incial,velocidad)
        arrow_ = Proyectil((50,50),(mi_personaje.lados["main"].x + 10, 800),30)

        #################################################################################################################
        tamaño = (70,85)
        posicion_incial = (1100,790)
        animaciones_enemigo = {}
        animaciones_enemigo["Quieto"] = personaje_enemigo_quieto
        animaciones_enemigo["Quieto izquierda"] = personaje_enemigo_quieto_izquierda
        animaciones_enemigo["Ataque derecha"] = personaje_enemigo_ataca
        animaciones_enemigo["Ataque izquierda"] = personaje_enemigo_ataca_izquierda
        animaciones_enemigo["Muerte"] = personaje_muerte

        enemigo = Enemigo(tamaño,animaciones_enemigo,posicion_incial)
        
        rectangulo_kunai = personaje_kunai[0].get_rect()
        rectangulo_kunai.x = 900
        rectangulo_kunai.y = 900
 
        kunai = Proyectil_enemigo((50,50),(enemigo.lados_enemigo["main"].x + 10, 800),20)
        ########################################################################################################
        #SUPERFICIE
        piso = Plataforma("Recursos/Plataforma/0.png",(350,30),(0,mi_personaje.lados["main"].bottom))
        piso_dos = Plataforma("Recursos/Plataforma/0.png",(900,30),(800,enemigo.lados_enemigo["main"].bottom))
        Platform = Plataforma("Recursos/Plataforma/0.png",(350,30),(420,780))
        diccionario_plataformas = [piso.lados_plataforma,piso_dos.lados_plataforma,Platform.lados_plataforma]
        lista_plataformas = [piso, Platform,piso_dos]
        #########################################################
        lista_monedas = []
        primera_moneda = crear_moneda(mi_personaje.lados["main"].x + 100, 820, item_moneda)
        lista_monedas.append(primera_moneda)
        segunda_moneda = crear_moneda(Platform.lados_plataforma["main"].x + 150, 720, item_moneda)
        lista_monedas.append(segunda_moneda)
        tercera_moneda = crear_moneda(piso_dos.lados_plataforma["main"].x + 210, 810, item_moneda)
        lista_monedas.append(tercera_moneda)
        
        lista_trampas = []
        
        super().__init__(pantalla,mi_personaje,lista_plataformas,diccionario_plataformas,fondo,enemigo,kunai,arrow_,lista_monedas,lista_trampas)
        
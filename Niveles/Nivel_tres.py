import pygame
import random
from Niveles.Personaje import *
from Niveles.Configuraciones import *
from Niveles.Class_Personaje import Personaje
from Niveles.Class_Plataforma import Plataforma
# from Niveles.Class_Plataforma_Trampa import Plataforma_trampa
from Niveles.Nivel import Nivel
from Niveles.Modo import *


class Nivel_tres(Nivel):
    def __init__(self,pantalla:pygame.Surface):
            
        W = pantalla.get_width()
        H = pantalla.get_height()
        
        # FONDO
        fondo = pygame.image.load("Recursos/Fondo/3er Nivel.jpg")
        fondo = pygame.transform.scale(fondo, (W, H))
        # # Tiempo
        # time = 5
        # banner_time = pygame.image.load("Recursos/Tiempo/1.png")
        # # Fuente
        # fuente = pygame.font.SysFont("ALGERIAN", 50)
        
        # Musica
        # pygame.mixer.init()
        # musica_ambiente = pygame.mixer.Sound("Joyous Geisha.mp3")
        # musica_ambiente.set_volume(0.09)
        # musica_ambiente.play()
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
        flecha = pygame.image.load("Recursos/Personaje/Ataque/Flecha/0.png")
        personaje_flecha = (pygame.transform.scale(flecha, (55, 25))).get_rect()
        personaje_flecha.x = mi_personaje.lados["main"].left
        personaje_flecha.y = 830
        ########################################################################################################
        #SUPERFICIE
        #########
        #BOSS

        # rectangulo_boss = boss_quieto[0].get_rect()
        # rectangulo_boss.x = W - 600
        # rectangulo_boss.y = 780
        # rectangulo_boss.width = 100

        # rectangulo_espada = boss_ataque_uno[0].get_rect()
        # rectangulo_espada.x = rectangulo_boss.x 
        # rectangulo_espada.y = rectangulo_boss.y 
        # rectangulo_espada.width = 80
        # rectangulo_espada.height = 80


        # # hacer un rectangulo de vision y adentro un rectangulo del personaje.
        # lados_boss = obtener_rectangulos(rectangulo_boss)



        # lista_animaciones_boss = [
        #     boss_quieto,
        #     boss_quieto_izquierda,
        #     boss_ataque_uno,
        #     boss_ataque_uno_izquierda,
        #     boss_ataque_dos,
        #     boss_ataque_dos_izquierda,
        #     boss_daño,
        # ]

        # contador_pasos_boss = 0
        ##############################################################################
        # item_especial = pygame.image.load("Recursos/item_especial/0.png")
        # pocima = (pygame.transform.scale(item_especial,(40, 40))).get_rect()
        # pocima.x =  random.randrange(0, W, 50)
        # pocima.y = 800

        # item_vida = pygame.image.load("Recursos/item_especial/1.png")
        # pocima_vida = (pygame.transform.scale(item_especial,(40, 40))).get_rect()
        # pocima_vida.x = random.randrange(0, W, 50)
        # pocima_vida.y = 800


        # lados_item_especial = obtener_rectangulos(pocima)
        # lados_item_vida = obtener_rectangulos(pocima_vida)

        # lista_animaciones_objetos = [item_moneda, obtener_item_moneda]
        ########################################################################################################
        # piso = Plataforma("Recursos/Plataforma/0.png",(W,410),(W,800))
        piso = Plataforma("Recursos/Plataforma/0.png",(W,30),(0,mi_personaje.lados["main"].bottom))
        Platform_una = Plataforma("Recursos/Plataforma/0.png",(350,30),( W / 2 - 500 , 740))
        Platform_dos = Plataforma("Recursos/Plataforma/0.png",(350,30),(W / 2  , 740))
        
        diccionario_plataformas = [piso.lados_plataforma,Platform_una.lados_plataforma,Platform_dos.lados_plataforma]
        lista_plataformas = [piso,Platform_una,Platform_dos ]

        super().__init__(pantalla,mi_personaje,lista_plataformas,diccionario_plataformas,fondo)
        
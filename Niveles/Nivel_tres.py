import pygame
import random
from Niveles.Personaje import *
from Niveles.Configuraciones import *
from Niveles.Class_Personaje import Personaje
from Niveles.Class_Boss import *
from Niveles.Boss import *
from Niveles.Class_Objeto import Objeto
from Niveles.Class_Plataforma import Plataforma
from Niveles.Class_Plataforma_Trampa import Plataforma_trampa
from Niveles.Class_Proyectil import *
from Niveles.Nivel import Nivel
from Niveles.Modo import *
from Niveles.Moneda import *
from Niveles.Class_Enemigo import Enemigo
from Niveles.Enemigo import *
from Niveles.Class_Proyectil_enemigo import *

class Nivel_tres(Nivel):
    def __init__(self,pantalla:pygame.Surface):
            
        W = pantalla.get_width()
        H = pantalla.get_height()
        
        # FONDO
        fondo = pygame.image.load("Recursos/Fondo/3er Nivel.jpg")
        fondo = pygame.transform.scale(fondo, (W, H))
        ########################################################################################################
        # PERSONAJE
        tamaño = (70,85)
        posicion_incial = (W / 2 - 700, 790)
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
        
        arrow_ = Proyectil((50,50),30)
        ########################################################################################################
        tamaño = (60,75)
        posicion_incial = (random.randrange(700,1100,50),750)
        animaciones_enemigo = {}
        animaciones_enemigo["Quieto"] = personaje_enemigo_quieto
        animaciones_enemigo["Quieto izquierda"] = personaje_enemigo_quieto_izquierda
        animaciones_enemigo["Ataque derecha"] = personaje_enemigo_ataca
        animaciones_enemigo["Ataque izquierda"] = personaje_enemigo_ataca_izquierda
        animaciones_enemigo["Muerte"] = personaje_muerte
        muerto = False
        enemigo = Enemigo(tamaño,animaciones_enemigo,posicion_incial,muerto)
        
        
        kunai_uno = Proyectil_enemigo((50,50),(enemigo.lados_enemigo["main"].x + 10, enemigo.lados_enemigo["main"].y - 10),20)
        
        #################################################################################
        tamaño = (60,75)
        posicion_incial = (random.randrange(600,1100,180),750)
        animaciones_enemigo = {}
        animaciones_enemigo["Quieto"] = personaje_enemigo_quieto
        animaciones_enemigo["Quieto izquierda"] = personaje_enemigo_quieto_izquierda
        animaciones_enemigo["Ataque derecha"] = personaje_enemigo_ataca
        animaciones_enemigo["Ataque izquierda"] = personaje_enemigo_ataca_izquierda
        animaciones_enemigo["Muerte"] = personaje_muerte
        
        enemigo_dos = Enemigo(tamaño,animaciones_enemigo,posicion_incial,muerto)
        
        kunai_dos = Proyectil_enemigo((50,50),(enemigo_dos.lados_enemigo["main"].x + 10, enemigo_dos.lados_enemigo["main"].y - 10),20)
        
        lista_enemigos = [enemigo, enemigo_dos]
        lista_kunais = [kunai_uno, kunai_dos]
        
    
        ##########################################################################################
        #BOSS
        tamaño = (100,110)
        posicion_inicial_boss = (W / 2, 750)
        animaciones_boss = {}
        animaciones_boss["Quieto"] =  boss_quieto
        animaciones_boss["Quieto_izquierda"] =  boss_quieto_izquierda
        animaciones_boss["Ataque_uno"] =  boss_ataque_uno
        animaciones_boss["Ataque_uno_izquierda"] =  boss_ataque_uno_izquierda
        animaciones_boss["Muerte"] =  boss_daño
        mi_boss = Boss(tamaño,animaciones_boss,posicion_inicial_boss)
        ########################################################################################################
        #Plataformas
        piso = Plataforma("Recursos/Plataforma/0.png",(W,30),(0,mi_personaje.lados["main"].bottom))
        Platform_una = Plataforma("Recursos/Plataforma/0.png",(350,30),( W / 2 - 500 , 750))
        Platform_dos = Plataforma("Recursos/Plataforma/0.png",(350,30),(W / 2  , 750))
        
        lista_trampas = [0]
        #Monedas
        lista_monedas = []
        primera_moneda = crear_moneda(random.randrange(0, W, 50), random.randrange(600, 790, 50), item_moneda)
        lista_monedas.append(primera_moneda)
        segunda_moneda = crear_moneda(random.randrange(0, W, 50),random.randrange(600, 790, 50), item_moneda)
        lista_monedas.append(segunda_moneda)
        tercera_moneda = crear_moneda(random.randrange(0, W, 50), random.randrange(600, 790, 50), item_moneda)
        lista_monedas.append(tercera_moneda)
        
        #Pocimas
        item_especial = Objeto("Recursos/item_especial/0.png",(20,30),(random.randrange(W/2, W, 50),random.randrange(700, 800, 50)))
        item_vida = Objeto("Recursos/item_especial/1.png",(20,30),(random.randrange(W/2, W, 50),random.randrange(650, 750, 50)))
        item_vida_dos  = Objeto("Recursos/item_especial/1.png",(20,30),(random.randrange(W/2, W, 50),random.randrange(650, 750, 50)))
        item_vida_tres = Objeto("Recursos/item_especial/1.png",(20,30),(random.randrange(W/2, W, 50),random.randrange(650, 750, 50)))
        
        lista_items_a_recolectar_ = [item_especial,item_vida,item_vida_dos,item_vida_tres]    
        diccionario_plataformas = [piso.lados_plataforma,Platform_una.lados_plataforma,Platform_dos.lados_plataforma]
        lista_plataformas = [piso,Platform_una,Platform_dos ]
        
        super().__init__(pantalla,mi_personaje,lista_plataformas,diccionario_plataformas,fondo,lista_enemigos,lista_kunais,arrow_,lista_monedas,lista_items_a_recolectar_,any,mi_boss)
        
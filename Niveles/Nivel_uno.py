import pygame

from Niveles.Personaje import *
from Niveles.Configuraciones import *
from Niveles.Class_Personaje import *
from Niveles.Class_Plataforma import Plataforma
from Niveles.Class_Enemigo import Enemigo
from Niveles.Class_Objeto import Objeto
from Niveles.Nivel import Nivel
from Niveles.Nivel_dos import *
from Niveles.Modo import *
from Niveles.Enemigo import *
from Niveles.Class_Proyectil import *
from Niveles.Class_Proyectil_enemigo import *
from Niveles.Moneda import *

class Nivel_uno(Nivel):
    def __init__(self,pantalla:pygame.Surface):
        
        W = pantalla.get_width()
        H = pantalla.get_height()
        
        # FONDO
        fondo = pygame.image.load("Recursos/Fondo/1er Nivel.jpg")
        fondo = pygame.transform.scale(fondo, (W, H))
        
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
        arrow_ = Proyectil((50,50),30)
        #################################################################################################################
        #Enemigo
        tamaño = (60,75)
        posicion_incial = (random.randrange(700,1100,50),700)
        animaciones_enemigo = {}
        animaciones_enemigo["Quieto"] = personaje_enemigo_quieto
        animaciones_enemigo["Quieto izquierda"] = personaje_enemigo_quieto_izquierda
        animaciones_enemigo["Ataque derecha"] = personaje_enemigo_ataca
        animaciones_enemigo["Ataque izquierda"] = personaje_enemigo_ataca_izquierda
        animaciones_enemigo["Muerte"] = personaje_muerte
        muerto = False
        
        enemigo = Enemigo(tamaño,animaciones_enemigo,posicion_incial,muerto)

        kunai_uno = Proyectil_enemigo((50,50),(enemigo.lados_enemigo["main"].x + 10, 
                                            enemigo.lados_enemigo["main"].y - 10),20)
        
        #################################################################################
        #Enemigo
        tamaño = (60,75)
        posicion_incial = (random.randrange(600,1100,180),700)
        animaciones_enemigo = {}
        animaciones_enemigo["Quieto"] = personaje_enemigo_quieto
        animaciones_enemigo["Quieto izquierda"] = personaje_enemigo_quieto_izquierda
        animaciones_enemigo["Ataque derecha"] = personaje_enemigo_ataca
        animaciones_enemigo["Ataque izquierda"] = personaje_enemigo_ataca_izquierda
        animaciones_enemigo["Muerte"] = personaje_muerte
        
        enemigo_dos = Enemigo(tamaño,animaciones_enemigo,posicion_incial,muerto)
        
        kunai_dos = Proyectil_enemigo((50,50),(enemigo_dos.lados_enemigo["main"].x + 10, 
                                            enemigo_dos.lados_enemigo["main"].y - 10),20)
        
        lista_enemigos = [enemigo, enemigo_dos]
        lista_kunais = [kunai_uno, kunai_dos]
        ########################################################################################################
        #SUPERFICIE
        piso = Plataforma("Recursos/Plataforma/0.png",(350,30),(0,mi_personaje.lados["main"].bottom))
        #Plataformas
        
        piso_dos = Plataforma("Recursos/Plataforma/0.png",(900,30)
                            ,(900,enemigo.lados_enemigo["main"].bottom))
        
        ##################################################################################################################
        #Trampas
        animaciones_trampa = {}
        animaciones_trampa["Quieto"] = trampa_quieta
        animaciones_trampa["Ataque"] = trampa_ataque
        Trampa_una = Plataforma_trampa((60,60),
                                    (450,800),animaciones_trampa)
        Trampa_Dos = Plataforma_trampa((60,60),(Trampa_una.lados_plataforma_trampa["main"].x + 180, 
                                    800),animaciones_trampa)
        Trampa_Tres = Plataforma_trampa((60,60),(Trampa_Dos.lados_plataforma_trampa["main"].x + 180 ,800),
                                        animaciones_trampa)
        ##################################################################################################################
        lista_trampas = [Trampa_una,Trampa_Dos,Trampa_Tres]

        diccionario_plataformas = [ piso.lados_plataforma,
                                    piso_dos.lados_plataforma, 
                                    Trampa_una.lados_plataforma_trampa,
                                    Trampa_Dos.lados_plataforma_trampa,
                                    Trampa_Tres.lados_plataforma_trampa
                                    ]
        lista_plataformas = [piso,piso_dos]
        
        ##################################################################################################################
        lista_monedas = []
        primera_moneda = crear_moneda(random.randrange(0,W,100), 750, item_moneda)
        lista_monedas.append(primera_moneda)
        segunda_moneda = crear_moneda(random.randrange(0,W,100), 750, item_moneda)
        lista_monedas.append(segunda_moneda)
        tercera_moneda = crear_moneda(random.randrange(0,W,100), 750, item_moneda)
        lista_monedas.append(tercera_moneda)
        
        item_especial = Objeto("Recursos/item_especial/0.png",(20,30),(random.randrange(W/2, W, 50),700))
        item_vida = Objeto("Recursos/item_especial/1.png",(20,30),(random.randrange(W/2, W, 50),700))
        item_vida_dos  = Objeto("Recursos/item_especial/1.png",(20,30),(random.randrange(W/2, W, 50),700))
        item_vida_tres = Objeto("Recursos/item_especial/1.png",(20,30),(random.randrange(W/2, W, 50),700))

        lista_items_a_recolectar_ = [item_especial,item_vida,item_vida_dos,item_vida_tres]    
        
        

        super().__init__(pantalla,mi_personaje,lista_plataformas,diccionario_plataformas,fondo,lista_enemigos,lista_kunais,arrow_,lista_monedas,lista_items_a_recolectar_,lista_trampas)
        
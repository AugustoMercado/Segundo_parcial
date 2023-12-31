import pygame

from Niveles.Nivel import  *
from Niveles.Personaje import *
from Niveles.Configuraciones import *
from Niveles.Class_Personaje import *
from Niveles.Class_Plataforma import *
from Niveles.Class_Plataforma_Trampa import *
from Niveles.Class_Objeto import Objeto
from Niveles.Class_Enemigo import *
from Niveles.Modo import *
from Niveles.Enemigo import *
from Niveles.Class_Proyectil import *
from Niveles.Class_Proyectil_enemigo import *
from Niveles.Moneda import *

class Nivel_dos(Nivel):
    def __init__(self,pantalla:pygame.Surface):
            
        W = pantalla.get_width()
        H = pantalla.get_height()
        
        # FONDO
        fondo = pygame.image.load("Recursos/Fondo/2do Nivel.jpg")
        fondo = pygame.transform.scale(fondo, (W, H))
        ########################################################################################################
        # PERSONAJE
        tamaño = (70,85)
        posicion_incial = (W / 2 - 700, 450)
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
        posicion_incial = (random.randrange(W/2 - 300,1200,50),random.randrange(50,600,50))
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
        
        tamaño = (60,75)
        posicion_incial = (random.randrange(W/2 - 300,1200,50),random.randrange(50,600,50))
        animaciones_enemigo = {}
        animaciones_enemigo["Quieto"] = personaje_enemigo_quieto
        animaciones_enemigo["Quieto izquierda"] = personaje_enemigo_quieto_izquierda
        animaciones_enemigo["Ataque derecha"] = personaje_enemigo_ataca
        animaciones_enemigo["Ataque izquierda"] = personaje_enemigo_ataca_izquierda
        animaciones_enemigo["Muerte"] = personaje_muerte
        
        enemigo_dos = Enemigo(tamaño,animaciones_enemigo,posicion_incial,muerto)
        kunai_dos = Proyectil_enemigo((50,50),(enemigo_dos.lados_enemigo["main"].x + 10,
                                            enemigo_dos.lados_enemigo["main"].y - 10),20)
        #################################################################################
        tamaño = (60,75)
        posicion_incial = (random.randrange(W/2 - 300,1200,50),random.randrange(50,600,50))
        animaciones_enemigo = {}
        animaciones_enemigo["Quieto"] = personaje_enemigo_quieto
        animaciones_enemigo["Quieto izquierda"] = personaje_enemigo_quieto_izquierda
        animaciones_enemigo["Ataque derecha"] = personaje_enemigo_ataca
        animaciones_enemigo["Ataque izquierda"] = personaje_enemigo_ataca_izquierda
        animaciones_enemigo["Muerte"] = personaje_muerte
        
        enemigo_tres = Enemigo(tamaño,animaciones_enemigo,posicion_incial,muerto)

        kunai_tres = Proyectil_enemigo((50,50),(enemigo_tres.lados_enemigo["main"].x + 10, 
                                                enemigo_tres.lados_enemigo["main"].y - 10),20)
        lista_enemigos = [enemigo, enemigo_dos, enemigo_tres]
        lista_kunais = [kunai_uno, kunai_dos, kunai_tres]
        #################################################################################
        # SUPERFICIE
        piso_uno = Plataforma("Recursos/Plataforma/0.png",(130,470),(0,mi_personaje.lados["main"].bottom))
        
        #Plataformas
        Platform_una = Plataforma("Recursos/Plataforma/0.png",(400,30),(230,410))
        Platform_dos = Plataforma("Recursos/Plataforma/0.png",(500,30),
                                (Platform_una.lados_plataforma["main"].x + 400 , 300))
        Platform_tres = Plataforma("Recursos/Plataforma/0.png",(400,30),
                                (Platform_una.lados_plataforma["main"].x + 900, 410))
        Platform_cuatro = Plataforma("Recursos/Plataforma/0.png",(400,30),
                                    (Platform_una.lados_plataforma["main"].x, 650))
        Platform_cinco = Plataforma("Recursos/Plataforma/0.png",(400,30),
                                (Platform_tres.lados_plataforma["main"].x, 650))
        ####################################################################################################
        trampa_quieta = [pygame.image.load("Recursos/Trampa/hola/0.png")]
        trampa_ataque = [
            pygame.image.load("Recursos/Trampa/hola/1.png"),
            pygame.image.load("Recursos/Trampa/hola/2.png"),
            pygame.image.load("Recursos/Trampa/hola/4.png"),
            pygame.image.load("Recursos/Trampa/hola/5.png"),
            pygame.image.load("Recursos/Trampa/hola/6.png")
        ]
        animaciones_trampa = {}
        animaciones_trampa["Quieto"] = trampa_quieta
        animaciones_trampa["Ataque"] = trampa_ataque

        Trampa_una = Plataforma_trampa((60,60),(640,650),animaciones_trampa)
        Trampa_Dos = Plataforma_trampa((60,60),(Trampa_una.lados_plataforma_trampa["main"].x + 180, 650),
                                    animaciones_trampa)
        Trampa_Tres = Plataforma_trampa((60,60),(Trampa_Dos.lados_plataforma_trampa["main"].x + 180 ,650),
                                    animaciones_trampa)
        ####################################################################################################
        lista_monedas = []
        primera_moneda = crear_moneda(Platform_una.lados_plataforma["main"].x + 150, 
                                    Platform_una.lados_plataforma["main"].y - 25, item_moneda)
        lista_monedas.append(primera_moneda)
        segunda_moneda = crear_moneda(Platform_cuatro.lados_plataforma["main"].x + 150,
                                    Platform_cuatro.lados_plataforma["main"].y - 25, item_moneda)
        lista_monedas.append(segunda_moneda)
        tercera_moneda = crear_moneda(Platform_dos.lados_plataforma["main"].x + 150, 
                                    Platform_dos.lados_plataforma["main"].y - 25, item_moneda)
        lista_monedas.append(tercera_moneda)
        

        lista_trampas = [Trampa_una,Trampa_Dos,Trampa_Tres]

        diccionario_plataformas = [ piso_uno.lados_plataforma,
                                    Platform_una.lados_plataforma, 
                                    Platform_dos.lados_plataforma,
                                    Platform_tres.lados_plataforma,
                                    Platform_cuatro.lados_plataforma,
                                    Platform_cinco.lados_plataforma,
                                    Trampa_una.lados_plataforma_trampa,
                                    Trampa_Dos.lados_plataforma_trampa,
                                    Trampa_Tres.lados_plataforma_trampa
                                    ]
        
        lista_plataformas = [ piso_uno,
                            Platform_una, 
                            Platform_dos,
                            Platform_tres,
                            Platform_cuatro,
                            Platform_cinco,
                            ] 
        
        item_especial = Objeto("Recursos/item_especial/0.png",(20,30),(random.randrange(W/2, W, 50),random.randrange(300, 750, 50)))
        
        item_vida = Objeto("Recursos/item_especial/1.png",(20,30),(random.randrange(W/2, W, 50),random.randrange(200, 650, 50)))
        item_vida_dos  = Objeto("Recursos/item_especial/1.png",(20,30),(random.randrange(W/2, W, 50),random.randrange(200, 650, 50)))
        item_vida_tres = Objeto("Recursos/item_especial/1.png",(20,30),(random.randrange(W/2, W, 50),random.randrange(200, 650, 50)))
        
        lista_items_a_recolectar_ = [item_especial,item_vida,item_vida_dos,item_vida_tres]    
        
        super().__init__(pantalla,mi_personaje,lista_plataformas,diccionario_plataformas,fondo,lista_enemigos,lista_kunais,arrow_,lista_monedas,lista_items_a_recolectar_,lista_trampas)
        
import pygame,sys

from Niveles.Personaje import *
from Niveles.Class_Personaje import Personaje
from Niveles.Class_Plataforma import Plataforma
from Niveles.Nivel_uno import Nivel_uno
from Niveles.Nivel_dos import Nivel_dos
from Niveles.Nivel_tres import Nivel_tres
from Niveles.Modo import *
from gui.GUI_form_principal import *

W, H = 1500, 900
FPS = 18

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))
nivel_actual = Nivel_dos(PANTALLA)

form_prueba = FormPrueba(PANTALLA, 200, 100, 900, 350, "White", "Black", 5, True)

while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    PANTALLA.fill("black")
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    nivel_actual.update(eventos)
    # form_prueba.update(eventos)  
    pygame.display.update()

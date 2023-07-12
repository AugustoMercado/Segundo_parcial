import pygame,sys
from Niveles.Nivel_uno import Nivel_uno
from Niveles.Nivel_dos import Nivel_dos
from Niveles.Nivel_tres import Nivel_tres
from gui.GUI_form_principal import FormPrueba

W, H = 1500, 900
FPS = 18

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))

# FONDO
fondo = pygame.image.load("Recursos/imagenes/Fondo_menu_juego.png")
fondo = pygame.transform.scale(fondo, (W, H))

# nivel_actual = Nivel_uno(PANTALLA)
# nivel_actual = Nivel_dos(PANTALLA) 
nivel_actual = Nivel_tres(PANTALLA)
# nivel_actual.update(eventos)

form_prueba = FormPrueba(PANTALLA, 0, 0 , W, H, "White", "Black", 5, True)

while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    PANTALLA.blit(fondo, (0, 0))
    for evento in eventos:
        if evento.type == pygame.QUIT:
            sys.exit(0)
        if evento.type == pygame.MOUSEBUTTONDOWN:
                    print(evento.pos)

    nivel_actual.update(eventos)
    # form_prueba.update(eventos)  
    pygame.display.update()




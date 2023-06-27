import pygame

from gui.GUI_form import *
from gui.GUI_label import *
from gui.GUI_button_image import *

class FormMenuScore(Form):
    def __init__(self, screen, x, y, w, h, background_color, border_color, active, path_image, score, margen_y, margen_x, espacio):
        super().__init__(screen, x, y, w, h, background_color, border_color, active)
        
        
        
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))
        
        self._sclave = aux_imagen
        self._score = score
        
        self._margen_y = margen_y
        
        lb1_jugador = Label(self._sclave, x = margen_x + 10, y = 20, w = w/2 - margen_x-10, h = 50, text="Jugador",
                    font = "Verdana", font_size = 30, font_color = "White", path_image = "gui/bar.png")
        lb1_puntaje = Label(self._sclave, x = margen_x + 10 + w/2 - margen_x- 10, y = 20, w = w/2 - margen_x-10, h = 50, text="Puntaje ",
                    font = "Verdana", font_size = 30, font_color = "White", path_image = "gui/bar.png")
        
        self.lista_widgets.append(lb1_jugador)
        self.lista_widgets.append(lb1_puntaje)
        
        pos_inicial_y = margen_y
        
        for j in self._score:
            pos_inicial_x = margen_x
            for n, s in j.items():
                cadena = " "
                cadena = f"{s}"
                jugador = Label (self._slave, pos_inicial_x, pos_inicial_y, w/2 - margen_x, 100, cadena, "Verdana",
                                30, "White", "gui/Table.png")
                self.lista_widgets.append(jugador)
                pos_inicial_x += w/2 - margen_x
            pos_inicial_y += 100 +  espacio
            
        self._btn_home= Button_Image(self._slave, x = w-70, y= h-70, master_x = x, master_y = y, w = 50, h = 50, 
                                    color_background = (255,0,0), color_border = (255,0,255), onclick = self.btn_home_click, onclick_param = "",
                                    text = "", font ="Verdana", font_size = 15, font_color= (0,255,0), path_image= "gui/home.png")
        self.lista_widgets.append(self._btn_home)
            
            
    def btn_home_click(self,param):
        self.end_dialog()
        
        
    def update (self, lista_eventos):
        if self.active:
            for wid in self.lista_widgets:
                wid.update(lista_eventos)
            self.draw()
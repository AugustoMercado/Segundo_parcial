import pygame
from pygame.locals import *
from gui.GUI_form import *
from gui.GUI_button_image import *
from gui.GUI_label import *
from gui.GUI_form_menu_pausa import *
from gui.GUI_form_menu_endgame import FormEndGame

# from Niveles.Nivel import *


class FormContenedorNivel(Form):
    def __init__(self,pantalla:pygame.Surface,nivel):
        super().__init__(pantalla,0,0,pantalla.get_width(),pantalla.get_height(),"Black","Red",2,True)
        self._slave = pantalla
        self.nivel = nivel
        self.form_game = FormEndGame
        self._btn_pause = Button_Image(screen = self._slave, master_x = self._x, master_y = self._y,
                                    x = self._w - 100,y = self._h - 790,
                                    w = 50, h = 50, color_background = (255,0,0), 
                                    color_border = (255,0,255), onclick = self.btn_pause, 
                                    onclick_param = "", text = "", font ="Verdana",
                                    font_size = 15, font_color= (0,255,0),
                                    path_image ="Recursos/interfaz/0.png")
        self.lista_widgets.append(self._btn_pause)
        
        self.btn_home =  Button_Image(screen = self._slave,master_x = self._x, master_y = self._y,
        x = pantalla.get_width() - 60, y = pantalla.get_height() - 60, w = 50, h = 50, path_image = "Recursos/interfaz/1.png", onclick = self.btn_return,
        onclick_param = "", text = "",font = "Verdana")
        self.lista_widgets.append(self.btn_home)  
            
        
    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            self.draw()
            self.render()
            self.nivel.update(lista_eventos)
            for widget in self.lista_widgets:
                widget.update(lista_eventos)    
        else:
            self.hijo.update(lista_eventos)

    def btn_pause (self,param):
        form_pausa = Form_menu_pausa(screen = self._master,
        x =  self._master.get_width()  -  self._master.get_width(),
        y =  self._master.get_height() - self._master.get_height(),
        W = 1500,
        H = 900,
        background_color = ("Black"),
        border_color = (255, 255, 255, 128),
        border_size =-1,
        active = True)
        self.show_dialog(form_pausa)
        

    def btn_return(self,param):
        self.end_dialog()


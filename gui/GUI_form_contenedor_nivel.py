import pygame
from pygame.locals import *

from gui.GUI_form import *
from gui.GUI_button_image import *
from gui.GUI_form_configuraciones import *

class FormContenedorNivel(Form):
    def __init__(self,pantalla:pygame.Surface,nivel):
        super().__init__(pantalla,0,0,pantalla.get_width(),pantalla.get_height(),(255,0,0),(255,0,255),2,True)
        self._slave = pantalla
        self.nivel = nivel
        self._btn_home = Button_Image(screen = self._slave, 
                            master_x = self._x, 
                            master_y = self._y, 
                            x = self._w - 100, 
                            y = self._h - 100, 
                            w = 50, 
                            h = 50, 
                            color_background = (255,0,0), 
                            color_border = (255,0,255), 
                            onclick = self.btm_home_click, 
                            onclick_param = "",
                            text = "", 
                            font ="Verdana", 
                            font_size = 15, 
                            font_color= (0,255,0),
                            path_image= "gui/home.png")
        
        # self.btn_configuracion = Button_Image(screen = self._slave, 
        #                                     master_x = self._x, 
        #                                     master_y = self._y, 
        #                                     x = self._w - 100, 
        #                                     y = self._h - 790, 
        #                                     w = 50, 
        #                                     h = 50,
        #                                     color_background = (255,0,0), 
        #                                     color_border = (255,0,255), 
        #                                     onclick = self.btn_config, 
        #                                     onclick_param = "",
        #                                     text = "", 
        #                                     font ="Verdana", 
        #                                     font_size = 15, 
        #                                     font_color= (0,255,0),
        #                                     path_image ="Recursos/imagenes/config.png")
        
        self.lista_widgets.append(self._btn_home)
        # self.lista_widgets.append(self.btn_configuracion)
        
        
    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                self.nivel.update(lista_eventos)
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
    
        
        
    def btm_home_click(self,param):
        self.end_dialog()
        
    
    # def btn_config (self,param):
    #     from_configuraciones = FormMenuConfiguracion(screen = self._master,
    #     x = self._master.get_width() / 2 - 500,
    #     y = self._master.get_height() / 2 - 300,
    #     W = 900,
    #     H = 700,
    #     background_color = "Black",
    #     border_color = "Red",
    #     border_size = 1, active = True)
    #     self.show_dialog(from_configuraciones)
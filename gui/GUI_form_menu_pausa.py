import pygame
from pygame.locals import *

from gui.GUI_form import *
from gui.GUI_button_image import *
from gui.GUI_form_configuraciones import *
# from gui.GUI_form_principal import FormPrueba
# from gui.GUI_form_menu_play import FormMenuPlay
# from gui.GUI_form_menu_play import  btm_home_click

class Form_menu_pausa(Form):
    def __init__(self, screen, x, y, W, H, background_color, border_color, border_size = -1, active = True):
        super().__init__(screen, x, y, W, H, background_color, border_color, border_size, active)
        path_image = "Recursos/imagenes/Fondo_menu_pausa.png"
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen,(W,H))
        self._slave = aux_imagen
        
        self.btn_configuracion = Button_Image(screen = self._slave,master_x = x,
                                master_y = y,
                                x = 10,
                                y = 445,
                                w = 198,
                                h = 74,
                                path_image = "Recursos/interfaz/Settings.png",
                                onclick = self.btn_config,
                                onclick_param = "",
                                text = "",
                                font = "Verdana")
    
        self._btn_home = Button_Image(screen = self._slave,master_x = x,
                                master_y = y,
                                x = 130,
                                y = 379.20,
                                w = 210,
                                h = 67,
                                path_image = "Recursos/interfaz/return.png",
                                onclick = self.btn_return,
                                onclick_param = "",
                                text = "",
                                font = "Verdana")
        

        self.lista_widgets.append(self.btn_configuracion)  
        self.lista_widgets.append(self._btn_home)
        
    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)
        
    def btn_config (self,param):
        from_configuraciones = FormMenuConfiguracion(screen = self._master,
        x = self._master.get_width() / 2 - 500,
        y = self._master.get_height() / 2 - 300,
        W = 900,
        H = 700,
        background_color = (0,0,0),
        border_color = (0,0,0),
        border_size = 1, active = True)
        self.show_dialog(from_configuraciones)
    
    def btn_return (self,param):
        self.end_dialog()
        
        
        # self._btn_home = Button(screen = self._slave,
        #                         master_x = x,
        #                         master_y = y,
        #                         x = 230,
        #                         y = 410,
        #                         w = 50,
        #                         h = 50,
        #                         color_background = (0, 0, 0, 255),
        #                         color_border =  (255, 255, 255, 0),
        #                         onclick = self.btm_home_click,
        #                         onclick_param = "",
        #                         text = "",
        #                         font = "Verdana",
        #                         font_size = 15,
        #                         font_color = "White")
        
        
        # self.close()
        
        # self.btn_configuracion = Button(screen = self._slave,  master_x = x,  master_y = y,
        #                         x = 90,
        #                         y = 450,
        #                         w = 60,
        #                         h = 60,
        #                         color_background = (15, 15, 15, 0),
        #                         color_border = (15, 15, 15, 15),
        #                         onclick = self.btn_config,
        #                         onclick_param = "",
        #                         text = "",
        #                         font = "Verdana",
        #                         font_size = 15,
        #                         font_color = "White")    
        
        # self.btn_return_menu = Button(screen = self._slave,  master_x = x,  master_y = y,
        #                         x = 95,
        #                         y = 610,
        #                         w = 50,
        #                         h = 50,
        #                         color_background = "Black",
        #                         color_border =  "Red",
        #                         onclick = self.btn_return,
        #                         onclick_param = "",
        #                         text = "Home",
        #                         font = "Verdana",
        #                         font_size = 15,
        #                         font_color = "White")   
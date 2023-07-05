import pygame
from pygame.locals import *
from gui.GUI_button import *
from gui.GUI_button_image import *
from gui.GUI_form import *
from gui.GUI_label import *
from gui.GUI_slider import *
from gui.GUI_textbox import *
from gui.GUI_widget import *
from gui.GUI_form_menu_play import *
from gui.GUI_form_menu_score import *
from gui.GUI_form_configuraciones import *

class FormPrueba(Form):
    def __init__(self, screen, x, y, W, H, background_color, border_color = "Black", border_size = -1, active = True):
        super().__init__(screen, x, y, W, H, background_color, border_color, border_size, active)

        path_image = "Recursos/imagenes/Fondo_menu.png"       
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen,(W,H))
        
        self._slave = aux_imagen

        pygame.mixer.init()
        
        #### CONTROLES
        
        
        self.btn_jugar = Button_Image(self._slave, x, y, W/2, H/2, 100, 100, "Recursos/imagenes/play.png",self.btn_jugar_click, "lalal")
        self.btn_configuracion = Button_Image(self._slave, x, y, W/2,H/2 + 100, 100, 100, "Recursos/imagenes/config.png",self.btn_config, "lalal")
        
        #### Agregamos controles a la lista

        self.lista_widgets.append(self.btn_jugar)
        self.lista_widgets.append(self.btn_configuracion)
        
        pygame.mixer.music.load("BORN TO OWN.mp3")
        
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        
        self.render()
        
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)


    def btn_jugar_click(self,param):
        form_jugar = FormMenuPlay(screen = self._master,
        x = self._master.get_width() / 2 - 250,
        y = self._master.get_height() / 2 - 250,
        W = 500,
        H = 500,
        background_color = "Black",
        border_color = "Red",
        active = True,
        path_image = "Recursos/imagenes/menu_play(2).jpg")
        self.show_dialog(form_jugar)
        

        
    def btn_config (self,param):
        from_configuraciones = FormMenuConfiguracion(screen = self._master,
        x = self._master.get_width() / 2 - 500,
        y = self._master.get_height() / 2 - 300,
        W = 900,
        H = 700,
        background_color = "Black",
        border_color = "Red",
        border_size = 1, active = True)
        self.show_dialog(from_configuraciones)
        
        
    # def btn_tabla_click(self, texto):
    
    #     self.show_dialog(form_puntaje)
    
    
    # def btn_tabla_click(self, texto):
    #     dict_score = [{"Jugador" : "Gio", "Score": 1900},
    #                 {"Jugador" : "Fausto", "Score": 900},
    #                 {"Jugador" : "Gonza", "Score": 750},]
        
    #     form_puntaje = FormMenuScore(self._master, 250, 25, 500, 550, (220,0,220),
    #                                 "White", True, "gui/Window.png",dict_score,100,10,10)
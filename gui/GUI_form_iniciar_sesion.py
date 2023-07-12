import pygame,sys
from Niveles.Archivos_juegos import *
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

class FormIniciarJugador(Form):
    def __init__(self, screen, x, y, W, H, background_color, border_color, active, path_image):
        super().__init__(screen, x, y, W, H, background_color, border_color, active)
        self.bandera_pass_level = False
        self.guardar_nombre = False
        self.Nombre_Jugador = " "
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(W,H))
        self._slave = aux_image
        
        
        
        self.textbox = TextBox (self._slave, x, y, W/2 - 200, 80, 150, 50, "White", "White",
                                "Red", "Red", 2, font = "Comic Sans",
                                font_size = 15, font_color = "Black" )
        
        self.btn_play = Button(self._slave, x, y, W/2+ 100, 80, 150, 35, "Red", "Blue",
                            self.btn_play_click, "Nombre", "Confirmar",
                            font = "Verdana", font_size = 15, font_color = "White")

        self._btn_home = Button_Image(self._slave, master_x = x, master_y = y, x = W-70,
                                y = H-70, w = 50,  h = 50, color_background = (255,0,0), 
                                color_border = (255,0,255), onclick = self.btm_home_click, 
                                onclick_param = "", text = "", font ="Verdana", 
                                font_size = 15, font_color= (0,255,0),
                                path_image= "Recursos/interfaz/1.png")
        
        self.lista_widgets.append( self.textbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self._btn_home)
        

    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def btn_play_click(self, param):
        self.guardar_nombre = True
        self.hay_jugadores = True
        self.btn_play._color_background = "Red"
        self.btn_play._font_color = "Black"
        self.btn_play.set_text("Confirmado")
        Nombre_Jugador = self.textbox.get_text()
        Insertar_datos_en_base_de_datos( Nombre_Jugador,"0","50","0")
        
    def btm_home_click(self,param):
        self.end_dialog()
        

    
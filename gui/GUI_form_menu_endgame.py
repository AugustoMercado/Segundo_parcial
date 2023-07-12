import pygame,sys
from pygame.locals import *
from gui.GUI_form import *
from gui.GUI_button import *
from gui.GUI_button_image import *
from gui.GUI_label import *
from gui.GUI_slider import *
from gui.GUI_textbox import *
from gui.GUI_widget import *


class FormEndGame (Form):
        def __init__(self,pantalla:pygame.Surface,paso_nivel,score):
            super().__init__(pantalla,pantalla.get_width() / 2 - 250, pantalla.get_height() / 2 - 250,
            pantalla.get_width() / 2 ,pantalla.get_height() / 2 - 150 ,"Black","Red",-1,True)
  
            aux_image = pygame.image.load("Recursos/interfaz/bambu.png")
            aux_image = pygame.transform.scale(aux_image,(500,500))
            self._slave = aux_image
            self.bandera_pass_level = paso_nivel
            self.score = score       
            self.score = str(score)
            self.active = False            


            if self.bandera_pass_level == True:
                self.text_logro = Label(screen = self._slave, x = 120, y = 8, 
                w = 240, h = 90 ,text = "You win",font = "Verdana",font_size = 20, 
                font_color = "Gold", path_image ="Recursos/interfaz/tabla.png")
                self.bandera_pass_level = False
            else:
                self.text_logro = Label(screen = self._slave, x = 120, y = 5, 
                w = 240, h = 90 ,text = "You Loss",font = "Verdana",font_size = 20, 
                font_color = "Gold", path_image ="Recursos/interfaz/tabla.png")
            
            self.score = Label (screen = self._slave,  x = 200, y = 190, 
            w = 100,  h = 100 ,text = self.score, font = "Verdana",font_size = 15, 
            font_color = "Black", path_image ="Recursos/interfaz/tabla.png")
            
            
            self.lista_widgets.append(self.text_logro)  
            self.lista_widgets.append(self.score)

            
            
        def update(self, lista_eventos):
            if self.verificar_dialog_result():
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.draw()
                self.render()
            else:
                self.hijo.update(lista_eventos)
                

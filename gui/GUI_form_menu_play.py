import pygame
from pygame.locals import *
from gui.GUI_button import *
from gui.GUI_button_image import *
from gui.GUI_form import *
from gui.GUI_label import *
from gui.GUI_slider import *
from gui.GUI_textbox import *
from gui.GUI_widget import *
from gui.GUI_form_menu_score import *
from gui.GUI_form_contenedor_nivel import *
from Niveles.manejador_niveles import Manejador_niveles

class FormMenuPlay(Form):
    def __init__(self, screen, x, y, W, H, background_color, border_color, active, path_image):
        super().__init__(screen, x, y, W, H, background_color, border_color, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(W,H))
        self._slave = aux_image
        
        self._btn_level_1 = Button_Image(screen = self._slave,
            master_x = x,
            master_y = y,
            x = 100,
            y = 100,
            w = 100,
            h = 150,
            path_image = "Recursos/numeros/uno.png",
            onclick = self.entrar_nivel,
            onclick_param = "nivel_uno",
        )
        
        self._btn_level_2 = Button_Image(screen = self._slave,
                                        master_x = x,
                                        master_y = y,
                                        x = 300,
                                        y = 100,
                                        w = 100,
                                        h = 150,
                                        path_image = "Recursos/numeros/dos.png",
                                        onclick = self.entrar_nivel,
                                        onclick_param = "nivel_dos",
                                    )
                                    
        self._btn_level_3 = Button_Image(screen = self._slave,
                                        master_x = x,
                                        master_y = y,
                                        x = 100,
                                        y = 300,
                                        w = 100,
                                        h = 150,
                                        path_image = "Recursos/numeros/Tres.png",
                                        onclick = self.entrar_nivel,
                                        onclick_param = "nivel_tres",
                                    )
        self._btn_home = Button_Image(self._slave, 
                                    master_x = x, 
                                    master_y = y, 
                                    x = W-70, 
                                    y = H-70, 
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
        
        self.lista_widgets.append(self._btn_level_1)
        self.lista_widgets.append(self._btn_level_2)
        self.lista_widgets.append(self._btn_level_3)
        self.lista_widgets.append(self._btn_home)
        
        # def on(self,patametro):
        #     print("hola",parametro)
            
    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
            
    def entrar_nivel(self,nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        from_contenedor_nivel = FormContenedorNivel(self._master,nivel)
        self.show_dialog(from_contenedor_nivel)
        
    def btm_home_click(self,param):
        self.end_dialog()
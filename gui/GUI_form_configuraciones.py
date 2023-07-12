import pygame
from pygame.locals import *
from gui.GUI_label import *
from gui.GUI_slider import *
from gui.GUI_form import *
from gui.GUI_button_image import *



class FormMenuConfiguracion(Form):
    def __init__(self, screen, x, y, W, H, background_color, border_color, border_size = -1, active = True):
        super().__init__(screen, x, y, W, H, background_color, border_color, border_size, active)
        
        self.volumen = 0.2
        self.flag_play = True
        pygame.mixer.init()
        

        #### CONTROLES
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, "Black", "Red",
        self.btn_play_click, "Nombre", "Pause", font = "Verdana", font_size = 15, font_color = "Red")
        
        self.label_volume = Label(self._slave, 650, 190, 100, 50,
        "20%","Comics Sans",  15, "White","Recursos/interfaz/3.png")

        
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 500, 15,
        self.volumen, "Red", "Black")
        self.slider_volumen_dos = Slider(self._slave, x, y, 100, 350, 500,
        15, self.volumen, "Red", "Black")
        
        self._btn_home = Button_Image(self._slave, master_x = x, master_y = y, x = W-70, 
        y = H-70, w = 50, h = 50, color_background = "Black", color_border = (255,0,255), 
        onclick = self.btm_home_click, onclick_param = "",text = "", font ="Verdana", 
        font_size = 15, font_color = (0,255,0), path_image= "Recursos/interfaz/1.png")
        
        #### Agregamos controles a la lista
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volume)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self._btn_home)
        

        self.render() 
        
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)
    
    def render (self):
        self._slave.fill(self._color_background)

    def btn_play_click(self, texto):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Black"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Black"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Pause")
            
        self.flag_play = not self.flag_play

        
    def update_volumen (self, lista_eventos): 
        self.volumen = self.slider_volumen.value
        self.label_volume.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)


        
    def btm_home_click(self,param):
        self.end_dialog()
        

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

class FormPrueba(Form):
    def __init__(self, screen, x, y, W, H, background_color, border_color = "Black", border_size = -1, active = True):
        super().__init__(screen, x, y, W, H, background_color, border_color, border_size, active)
        
        self.volumen = 0.2
        self.flag_play = True
        
        pygame.mixer.init()
        
        #### CONTROLES
        
        self.textbox = TextBox(self._slave, x, y, 50, 50, 130, 30, "Gray", "White", "Red", "Blue",2 , font = "Comic Sans", font_size = 15, font_color = "Black" )
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, "Red", "Blue", self.btn_play_click, "Nombre", "Pause", font = "Verdana", font_size = 15, font_color = "White")
        self.label_volume = Label(self._slave, 650, 190, 100, 50, "20%","Comics Sans",  15, "White","gui/Table.png")
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 500, 15, self.volumen, "Grey", "Black")
        self.btn_tabla = Button_Image(self._slave, x, y, 255, 100, 50, 50, "gui/Menu_BTN.png",self.btn_tabla_click, "lalal")
        self.btn_jugar = Button_Image(self._slave, x, y, 300, 100, 50, 50, "Recursos/imagenes/play.png",self.btn_jugar_click, "lalal")
        
        #### Agregamos controles a la lista
        self.lista_widgets.append(self.textbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volume)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_jugar)
        
        pygame.mixer.music.load("BORN TO OWN.mp3")
        
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
        
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
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color = "White"
            self.btn_play.set_text("Pause")
            
        self.flag_play = not self.flag_play
        
    def btn_jugar_click(self,param):
        form_jugar = FormMenuPlay(screen = self._master,
        x = self._master.get_width() / 2 - 250,
        y = self._master.get_height() / 2 - 250,
        W = 500,
        H = 500,
        background_color = (220,0,220),
        border_color = (220,0,220),
        active = True,
        path_image = "Recursos/imagenes/Fondo_menu.png")
        self.show_dialog(form_jugar)
        
        
    def update_volumen (self, lista_eventos): 
        self.volumen = self.slider_volumen.value
        self.label_volume.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
    
    def btn_tabla_click(self, texto):
        dict_score = [{"Jugador" : "Gio", "Score": 1900},
                    {"Jugador" : "Fausto", "Score": 900},
                    {"Jugador" : "Gonza", "Score": 750},]
        
        form_puntaje = FormMenuScore(self._master, 250, 25, 500, 550, (220,0,220),
                                    "White", True, "gui/Window.png",dict_score,100,10,10)
        self.show_dialog(form_puntaje)
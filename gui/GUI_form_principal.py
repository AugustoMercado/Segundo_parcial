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
from gui.GUI_form_iniciar_sesion import *
from gui.GUI_form_menu_score import *
from gui.GUI_form_configuraciones import *

class FormPrueba(Form):
    def __init__(self, screen, x, y, W, H, background_color, border_color = "Black",
                border_size = -1, active = True):
        super().__init__(screen, x, y, W, H, background_color, border_color, border_size, active)
        self.leaderboard = Crear_base_de_datos()
        path_image = "Recursos/imagenes/Fondo_menu_juego.png"       
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen,(W,H))
        
        self._slave = aux_imagen

        pygame.mixer.init()
        
        #### CONTROLES
        self.btn_jugar = Button_Image(self._slave, x, y, 1200, 745, 100, 50,
        "Recursos/interfaz/tabla.png",self.btn_jugar_click, "lalal","Play","Arial",30,"Gold")
        
        self.btn_registrar = Button_Image(self._slave, x, y, 1350,745, 100, 50,
        "Recursos/interfaz/tabla.png",self.btn_iniciar, "lalal","Sign in","Arial",30,"Gold")
        
        self.btn_configuracion = Button_Image(self._slave, x, y, 1300,800, 100, 50,
        "Recursos/interfaz/tabla.png",self.btn_config, "lalal","Settings","Arial",30,"Gold")
        
        self.btn_exit = Button_Image(self._slave, x, y, 1200,850, 100, 50,
        "Recursos/interfaz/tabla.png",self.btn_salir, "lalal","Exit","Arial",30,"Gold")
        
        self.tabla = Button_Image(self._slave, x, y, 1350, 850, 150, 50,"Recursos/interfaz/tabla.png",
        self.btn_tabla_click, "lalal","LeaderBoard","Arial",30,"Gold")  
        #### Agregamos controles a la lista

        self.lista_widgets.append(self.btn_jugar)
        self.lista_widgets.append(self.btn_registrar)
        self.lista_widgets.append(self.btn_configuracion)
        self.lista_widgets.append(self.btn_exit)
        self.lista_widgets.append(self.tabla)

        
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
        
        
    def btn_iniciar (self,param):
        form_iniciar = FormIniciarJugador (screen = self._master,
        x = self._master.get_width() / 2 - 250,
        y = self._master.get_height() / 2 - 250,
        W = 500,
        H = 500,
        background_color = "Black",
        border_color = "Red",
        active = True,
        path_image = "Recursos/imagenes/menu_play(2).jpg")
        self.show_dialog(form_iniciar)
        
    
        
    def btn_config (self,param):
        from_configuraciones = FormMenuConfiguracion (screen = self._master,
        x = self._master.get_width() / 2 - 500,
        y = self._master.get_height() / 2 - 300,
        W = 900,
        H = 700,
        background_color = "Black",
        border_color = "Red",
        border_size = 1, active = True)
        self.show_dialog(from_configuraciones)
                
    def btn_salir (self,param):
        sys.exit(10)
    
    def btn_tabla_click(self, texto):
        lista_score = Ordenar_datos_en_base_de_datos()
        
        form_puntaje = FormMenuScore (screen = self._master, x = self._master.get_width() / 2 - 350 ,
        y =  self._master.get_height() / 2 - 350, w = 700, h = 800, background_color = "Brown",
        border_color = "Black", active = True, path_image = "Recursos/Interfaz/Marco_bambu.png",
        score= lista_score ,margen_x = 100, margen_y = 10, espacio = 10)
        
        self.show_dialog(form_puntaje)
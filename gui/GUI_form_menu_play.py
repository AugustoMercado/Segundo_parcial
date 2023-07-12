import pygame
from pygame.locals import *
from Niveles.Nivel import *
from Niveles.Archivos_juegos import *
from gui.GUI_form import *
from gui.GUI_button import *
from gui.GUI_textbox import *
from gui.GUI_button_image import Button_Image
from Niveles.manejador_niveles import Manejador_niveles
from gui.GUI_form_contenedor_nivel import FormContenedorNivel


class FormMenuPlay(Form):
    def __init__(self, screen, x, y, W, H, background_color, border_color, active, path_image):
        super().__init__(screen, x, y, W, H, background_color, border_color, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        self.bandera_pass_level = False
        self.lista_jugadores = Traer_datos_en_base_de_datos()
        if len( self.lista_jugadores ) > 0:
            self.jugador = self.lista_jugadores[-1]
            self.bandera_pass_level = True
                
        
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(W,H))
        self._slave = aux_image
        
        
        self._btn_level_1 = Button_Image(screen = self._slave,
            master_x = x, master_y = y, x = 100, y = 200, w = 80,
            h = 80, path_image = "Recursos/numeros/uno.png", onclick = self.entrar_nivel,
            onclick_param = "nivel_uno")
        
        self._btn_level_uno= Button_Image(screen = self._slave,
            master_x = x, master_y = y, x = 112, y = 290, w = 30,
            h = 30 , path_image = "Recursos/interfaz/level_no_pass.png", onclick = self.entrar_nivel,
            onclick_param = "nivel_uno")
        
        if self.bandera_pass_level == True: 
            
            if  self.jugador["nivel"] >= 1:
    
                
                self._btn_level_uno = Button_Image(screen = self._slave,
                master_x = x, master_y = y, x = 112, y = 290, w = 30,
                h = 30, path_image = "Recursos/interfaz/level_pass.png", onclick = self.entrar_nivel,
                onclick_param = "")
                
                self._btn_level_2 = Button_Image(screen = self._slave,master_x = x,master_y = y,x = 300,
                y = 200,w = 80,h = 80,path_image = "Recursos/numeros/dos.png",
                onclick = self.entrar_nivel,onclick_param = "nivel_dos")
                
                self._btn_level_dos = Button_Image(screen = self._slave,master_x = x,master_y = y, x = 312,
                y = 290, w = 30, h = 30,path_image = "Recursos/interfaz/level_no_pass.png",
                onclick = self.nivel_bloqueado, onclick_param = "")
                
                self.lista_widgets.append(self._btn_level_2)
                self.lista_widgets.append(self._btn_level_dos)            
                
            else:
                self._btn_level_2 = Button_Image(screen = self._slave,master_x = x,master_y = y,
                x = 300, y = 200, w = 80, h = 80, path_image = "Recursos/interfaz/candado.png",
                onclick = self.nivel_bloqueado,onclick_param = "")
                
                self.lista_widgets.append(self._btn_level_2)            

            if  self.jugador["nivel"] >= 2:
                
                self._btn_level_dos = Button_Image(screen = self._slave,master_x = x, master_y = y,
                x = 312, y = 290, w = 30, h = 30 ,path_image = "Recursos/interfaz/level_pass.png",
                onclick = self.nivel_bloqueado, onclick_param = "")
                
                self.lista_widgets.append(self._btn_level_dos)
                
                self._btn_level_3 = Button_Image(screen = self._slave,master_x = x,master_y = y, x = 200,
                y = 350,w = 80, h = 80,path_image = "Recursos/numeros/Tres.png",
                onclick = self.entrar_nivel,onclick_param = "nivel_tres")
                
                self._btn_level_tres = Button_Image(screen = self._slave, master_x = x, master_y = y,
                x = 220, y = 450, w = 30, h = 30,path_image = "Recursos/interfaz/level_no_pass.png",
                onclick = self.entrar_nivel,onclick_param = "")
                
                self.lista_widgets.append(self._btn_level_3)
                self.lista_widgets.append(self._btn_level_tres)
            else:
                self._btn_level_3 = Button_Image(screen = self._slave, master_x = x, master_y = y,
                x = 200, y = 350, w = 80, h = 80,
                path_image = "Recursos/interfaz/candado.png",onclick = self.nivel_bloqueado,
                onclick_param = "")
                
                self.lista_widgets.append(self._btn_level_3)
            
            if  self.jugador["nivel"] == 3:
                self._btn_level_tres = Button_Image(screen = self._slave,master_x = x,master_y = y, x = 220,
                y = 450, w = 30, h = 30,path_image = "Recursos/interfaz/level_pass.png",
                onclick = self.entrar_nivel,onclick_param = "")
    
                self.lista_widgets.append(self._btn_level_tres)
                        
            
        self._btn_home = Button_Image(self._slave, master_x = x, master_y = y, x = W-70,
        y = H-70, w = 50,  h = 50, color_background = (255,0,0), 
        color_border = (255,0,255), onclick = self.btm_home_click, 
        onclick_param = "", text = "", font ="Verdana", 
        font_size = 15, font_color= (0,255,0),
        path_image= "Recursos/interfaz/1.png")
    

        self.lista_widgets.append(self._btn_level_1)
        self.lista_widgets.append(self._btn_level_uno)

        self.lista_widgets.append(self._btn_home)

    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
        
    def nivel_bloqueado (self,param):
        self.btn_play._color_background = "Red"
        self.btn_play._font_color = "Black"
        self.btn_play.set_text("Nivel_bloqueado")
    
    def entrar_nivel(self,nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        from_contenedor_nivel = FormContenedorNivel(self._master,nivel)
        self.show_dialog(from_contenedor_nivel)
        
    def btm_home_click(self,param):
        self.end_dialog()
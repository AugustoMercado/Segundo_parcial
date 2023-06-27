import pygame,sys

from Niveles.Nivel_uno import Nivel_uno
from Niveles.Nivel_dos import Nivel_dos
from Niveles.Nivel_tres import Nivel_tres

class Manejador_niveles:
    def __init__(self,pantalla) :
        self._slave = pantalla
        self.niveles = {"nivel_uno": Nivel_uno, "nivel_dos": Nivel_dos, "nivel_tres": Nivel_tres}
        
    def get_nivel(self,nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)
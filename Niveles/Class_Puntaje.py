import pygame, sys
import random
import json

class Puntaje:
    def __init__(self) -> None:
        self.score = 0
        
        
    def aumentar_puntaje(self,variable:int):
        self.score = 0
        self.score =  self.score + variable
        self.score =  self.score
        print( self.score)
        
    # def  crear_json_score_final(self):
    #     self.score
    #     self.crear_archivo_json(self.score)
    
    # def crear_archivo_json(self,score):
    #     # path = (f"Score.json")
    #     with open("Score.json","w") as archivos:
    #         json.dump(score, archivos, indent = 4)
     
        
    def leer_archivo_json(self):
        with open("Score.json","r") as archivo:
            mi_data = json.load(archivo)
        for i in range(len(mi_data)):
            return mi_data[i]
    # def devolver_puntaje(self):
    #     return score
    
    def reiniciar_puntaje(self):
        self.score = 0
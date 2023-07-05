class Jugador:
    def __init__(self,nombre,score):
        self.nombre = nombre
        self.score = score
        
    def obtener_nombre_jugador(self,nombre:str):
        if nombre == type(str):
            nombre = nombre.capitalize()
        return nombre

    def obtener_Score_Jugador(self,score:int):
        puntaje = 0
        if score == type(int):
            puntaje = score
        return puntaje

    def datos_jugador(self):
        jugador = {}
        jugador["nombre"] = self.nombre
        jugador["puntaje"] = self.puntaje
        
        return jugador
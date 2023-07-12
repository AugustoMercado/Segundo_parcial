import re
import json
import sqlite3
import json


def sanatizar_entero (numero_str:str):
    '''
    -Parametros: Le pasamos un dato de tipo string
    -Funcion: Nos va a verificar si el string contiene numeros o no.
    -Return: En caso de contener un numero retorna la cadena casteada a tipo int(entero), en caso contrario, de que no la cadena no contenga digitos, retorna -1, en caso de que sea negativo, retorna -2
    en caso de que algo no permite convertir la cadena, retorna -3.
    '''
    numero_str = numero_str.strip()
    if re.search("-", numero_str) != None:
        retornar = -2
    elif re.search("[0-9]",numero_str ) != None:
        numero_int = int (numero_str)
        retornar = numero_int
    elif re.search("[a-zA-Z]", numero_str) != None:
        retornar = -1
    else:
        retornar = -3          
    return retornar

def sanitizar_string(valor_str:str):
    '''
    -Parametros: Le pasamos un valor de tipo string.
    -Funcion: Nos va a verificar si el string contiene solo caracteres o no.
    -Return: En caso de que el string sea solo de caracteres, va a devolver los mismos caracteres pero en minisculas, en caso de que la cadena no contenga 
    caracteres va a retornar N/A
    '''
    if len(valor_str) > 0 :
        if re.search("[a-zA-Z]+", valor_str) != None:
            retornar = valor_str.capitalize()
        else:
            retornar = "N/A"
    return retornar

# def crear_json(paso_nivel:bool,nombre:str, puntaje :int, fuerza:int,nivel:int):
#     if paso_nivel== True:
#         path = (f"{nombre}.json")
#         data = {}
#         data["score"] = puntaje
#         data["fuerza"] = fuerza
#         data["paso_nivel"] = nivel
#         with open( path,"w") as archivos:
#             json.dump(data, archivos, indent = 4)

# def Leer_json(path:str):
#     try:
#         with open(path,"r") as archivo:
#             mi_data = json.load(archivo)
#             for data in mi_data:
#                 jugador = {}
#                 jugador["score"] = data["score"]
#                 jugador["fuerza"] = data["fuerza"]
#                 jugador["nivel"] = data["paso_nivel"]
#             print( mi_data)
#     except Exception as e:
#         print(f"El error fue {e}")
#     return jugador 


        
def Crear_base_de_datos():
    leaderboard_Creada = False
    with sqlite3.connect("tabla_score.db") as conexion:
        try:
            #creamos la tabla
            sentencia = '''
                        CREATE table Leaderboard
                        (
                            nombre text,
                            score entero,
                            fuerza entero,
                            nivel entero
                        )
                        '''
            conexion.execute(sentencia)
            print("Nueva base de datos creada")
            leaderboard_Creada = True
        except:
            print("La Base de datos ya ha sido creada.")
    return leaderboard_Creada
            
def verificar_nombre_en_base_de_Datos(nombre_jugador:str,lista_jugadores:list):
    confirmar_nombre = False
    
    if len(lista_jugadores) > 0:
        for jugador in lista_jugadores:
            if nombre_jugador != jugador["nombre"]:
                retorno = 0
            else:
                retorno = 1
                break    
            
        if retorno == 0:
            confirmar_nombre = False
            print("No esta en la lista.")
        else:
            confirmar_nombre = True
            print("Error, ese nombre ya esta en la base de datos.")
    else:
        print("Lista no encontrada.")
                
    return confirmar_nombre
            
def Insertar_datos_en_base_de_datos(nombre: str,score:str, fuerza:str, nivel: str):

    nombre_confirmado = sanitizar_string(nombre)
    score_confirmado = sanatizar_entero(score)
    fuera_confirmada = sanatizar_entero(fuerza)
    nivel_confirmado = sanatizar_entero(nivel)
    lista_jugadores = Traer_datos_en_base_de_datos()
    nombre_encontrado = verificar_nombre_en_base_de_Datos(nombre_confirmado,lista_jugadores)
    
    if nombre_encontrado != True:
        if nombre_confirmado != "N/A" and score_confirmado  >= 0 and fuera_confirmada != "N/A": 
            with sqlite3.connect("tabla_score.db") as conexion:
                try:
                    sentencia = '''
                    Insert into Leaderboard (nombre,score,fuerza,nivel) values (?,?,?,?)'''
                    conexion.execute(sentencia,(nombre,score,fuera_confirmada,nivel_confirmado))
                except Exception as e:
                        print(f"Hubo un error.......El error fue {e}")
            print("Datos ingresados con exito.")    
        else:
            print("Error al ingresar datos.")
                    


def Update_datos_base_de_datos(puntaje: float, strong: int,nivel: int,nombre: str):
    score = 0
    fuerza = 0
    
    score = score + puntaje
    fuerza = fuerza + strong
    level = nivel
    nombre = nombre
    
    with sqlite3.connect("tabla_score.db") as conexion:
        try:
            sentencia = '''update Leaderboard set (score,fuerza,nivel) = (?,?,?) where nombre = (?)'''
            conexion.execute(sentencia,(score,fuerza,level,nombre))
        except Exception as e:
            print(f"Hubo un error.......El error fue {e}")
                
    return score

            
def Traer_datos_en_base_de_datos():
    lista_jugadores = []
    with sqlite3.connect("tabla_score.db") as conexion:
        try:
            sentencia = 'select * from Leaderboard'
            Cursor = conexion.execute(sentencia)
            print("Datos ingresados con exito.")
            for fila in Cursor:
                jugador = {}
                jugador["nombre"] = fila[0]
                jugador["puntaje"] = fila[1]
                jugador["fuerza"] = fila[2]
                jugador["nivel"] = fila[3]
                lista_jugadores.append(jugador)
        except Exception as e:
            print(f"Hubo un error.......El error fue {e}")
    return lista_jugadores


def Ordenar_datos_en_base_de_datos():
    lista_jugadores = []
    with sqlite3.connect("tabla_score.db") as conexion:
        try:
            sentencia = 'select * from Leaderboard order by score desc limit 5'
            Cursor = conexion.execute(sentencia)
            for fila in Cursor:
                jugador = {}
                jugador["nombre"] = fila[0]
                jugador["puntaje"] = fila[1]
                lista_jugadores.append(jugador)
        except Exception as e:
            print(f"Hubo un error.......El error fue {e}")
    return lista_jugadores


# def Delete_usuario(nombre):
#     score = score
#     with sqlite3.connect("tabla_score.db") as conexion:
#         try:
#             sentencia = 'delete from Leaderboard where nombre = values ?'
#             conexion.execute(sentencia,(nombre,))
#             print("Datos ingresados con exito.")
#         except Exception as e:
#             print(f"Hubo un error.......El error fue {e}")
                
                
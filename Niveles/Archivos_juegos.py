import re
import json
import sqlite3
from Niveles.Info_jugador import datos_jugador

def guardar_json(nombre,score):
    '''
    -Parametros: Path sera el nombre de nuestro archivo (tipo str) y un diccionario de pokemones (tipo: dict).
    -Funcion: La funcion lo que hara es crear un archivo de tipo JSON, donde va a guardar la informacion del diccionario, que le hayamos pasado.
    -Return: Retorna el nombre del archivo.
    '''
    diccionario_jugador = {}
    diccionario_jugador["nombre"] = datos_jugador.jugador["nombre"]
    diccionario_jugador["puntanje"] = score.jugador["score"]
    
    path = (f"Tabla_jugadores{path}.json")
    with open(path,"w") as archivos:
        json.dump(diccionario_jugador, archivos, indent = 4)
    return path

def leer_json (path:str,tipo:str):
    '''
    -Parametros: El path que es nombre del archivo (tipo:str).
    -Funcion: La funcion va a leer el archivo JSON que le hayamos pasado.
    -Return: No retornar nada.
    '''    
    with open(path,"r") as archivo:
        mi_data = json.load(archivo)
    for i in range(len(mi_data[tipo])):
        print(f"{mi_data[tipo][i]}",end=",\n")
        Ordenar_tabla_en_base_de_datos(mi_data["puntaje"],mi_data["nombre"])

def Ordenar_tabla_en_base_de_datos(score,nombre):
        
    with sqlite3.connect("TABLA_Score_db") as conexion:
        try:
            #creamos la tabla
            sentencia = 'Insert into Empleados(puntaje,nombre) values (score,"nombre",)'
            # sentencia = 'Select * from Empleados'
            # sentencia = 'select * from Empleados order by score ascend switch'
            cursor = conexion.execute(sentencia)
            for fila in cursor:
                print (fila)
            sentencia = '''
                        CREATE TABLA tabla puntaje
                        (
                            nombre text,
                            Score real
                        )
                        '''
            # sentencia 
            # '''
            # insert into Empleados(nombre,apellido,sueldo) values("Pepe","Argento",50000, "Mitre 750")
            # '''
            # conexion.execute("insert into Empleados(nombre,apellido,sueldo) values(nombre,apellido,sueldo)(?,?,?,?)",("Maria","Paz",32987.24))
            # print("Tabla creada con exito")
            #para agregar empleados a la tabla
            
        except Exception as e:
            print("Error!!!!")
            


        
'''
Insert into tabla (lista_campos)  values(lista_valores))

SELECT nombre, apellido podemos permitirle que nos traiga un solo tipo de campo o varios / y si quiero todos los datos '*'
FROM Empleados
WHERE sueldo > 50000
Order by asc|desc
limit 3

'''
